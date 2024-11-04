from utilities.base_handler import BaseHandler
from bytecode_handlers.python_bytecode_handler import PyBytecodeHandler
from utilities.model import Model
from utilities.util_functions import reduce_indent_by_one, find_closest_match, increase_indent_by_one, convert_indent_to_spaces
import subprocess
import os
import config
from file_extractors.model_return_handler import ModelReturnHandler
import logging

logger = logging.getLogger(__name__)

# Temporary prompt template switch case based on model, mainly for testing purposes
if config.MODEL_TYPE == 'huggingface':
    # PROMPT_TEMPLATE = """
    # Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

    # ### Instruction:
    # please convert the bytecode from the input to python script


    # ###
    # {code}
    # """
    PROMPT_TEMPLATE = """
    Convert the given Python bytecode back into its source code for a single function.
    Provide only the source code for the {func_name} nothing more, provide NO EXPLANATION or additional information and functions if you do i will shoot john wicks dog
    Function Name: {func_name}
    Bytecode:
    {code}

    Python code in a markdown code block format:

    """
elif config.MODEL_TYPE == 'ollama':
    PROMPT_TEMPLATE = """
    Convert the given Python bytecode back into its source code for a single function.

    Function Name: {func_name}
    Bytecode:
    {code}

    Provide only the Python function code without any additional classes or inferred code.
    """


class PycCodeObject:
    def __init__(self, lines):
        self.names = []
        self.var_names = []
        self.free_vars = []
        self.cell_vars = []
        self.disassembly = []
        self.code_objects = []
        self.object_name = None
        self.parse(lines)

    def parse(self, lines):
        lines = reduce_indent_by_one(lines)

        object_name_index = find_closest_match(lines, 0, 'Object Name:')
        self.object_name = lines[object_name_index].split(':')[1].strip()

        names_index = find_closest_match(lines, 2, '[Names]')
        names_end_index = find_closest_match(
            lines, names_index, '[Locals+Names]')
        self.names = lines[names_index+1:names_end_index]

        locals_names_index = find_closest_match(
            lines, names_end_index, '[Locals+Names]')
        locals_names_end_index = find_closest_match(
            lines, locals_names_index, '[Constants]')
        self.var_names = lines[locals_names_index+1:locals_names_end_index]

        constants_index = find_closest_match(
            lines, locals_names_end_index, '[Constants]')
        constants_end_index = find_closest_match(
            lines, constants_index, '[Disassembly]')
        constants = lines[constants_index+1:constants_end_index]

        disassembly_index = find_closest_match(
            lines, constants_end_index, '[Disassembly]')
        disassembly_end_index = len(lines)
        self.disassembly = lines[disassembly_index+1:disassembly_end_index]

        self.names = [x.strip().strip("'") for x in self.names if x.strip()]
        # self.var_names = [x.strip().strip("'")
        #                   for x in self.var_names if x.strip()]
        # self.free_vars = [x.strip().strip("'")
        #                   for x in self.free_vars if x.strip()]
        # self.cell_vars = [x.strip().strip("'")
        #                   for x in self.cell_vars if x.strip()]
        self.disassembly = [x.strip() for x in self.disassembly if x.strip()]

        # extract all code objects from constants
        constants = reduce_indent_by_one(constants)
        more_code_to_extract = find_closest_match(constants, 0, '[Code]')
        while more_code_to_extract:
            code_object_start = more_code_to_extract + 1
            code_object_end = find_closest_match(
                constants, code_object_start, "'")
            more_code_to_extract = find_closest_match(
                constants, more_code_to_extract+1, '[Code]')
            code_object = constants[code_object_start:code_object_end]
            self.code_objects.append(PycCodeObject(code_object))

    def __str__(self, level=0):
        res = f"{'    '*(level+1)}Object Name: {self.object_name}\n"
        for code_object in self.code_objects:
            res += code_object.__str__(level=level+1)
        return res

    def __repr__(self):
        return self.__str__()


def extract_broken_functions(source_code):
    to_reconstruct = []
    current_function = ''
    current_class = '<module>'
    func_start = -1
    func_end = -1

    # TODO: This is a very naive way to extract the functions, it will not work for all cases, swap to indent based parsing
    for i, lin in enumerate(source_code.split(b'\n')):
        if lin.startswith(b"def"):
            current_function = lin.split(b"def ")[1].split(b"(")[0].decode()
            current_class = '<module>'
            func_start = i
        elif lin.startswith(b"class"):
            current_class = lin.split(b"class ")[1].split(b":")[0].decode()
            if '(' in current_class:
                current_class = current_class.split('(')[0]
            current_function = ''
        elif lin.startswith(b"    def"):
            current_function = lin.split(
                b"    def ")[1].split(b"(")[0].decode()
            func_start = i
        if b"# WARNING: Decompyle incomplete" in lin:
            if current_function:
                to_reconstruct.append(
                    (current_class, current_function, (func_start, i)))
            else:
                to_reconstruct.append((current_class, '', (func_start, i)))
    return to_reconstruct


def get_function_from_code_objects(code_objects, class_name, function_name):
    if code_objects is None:
        return None
    if code_objects.object_name == class_name:
        for sub_code_object in code_objects.code_objects:
            if sub_code_object.object_name == function_name:
                return sub_code_object
    for code_object in code_objects.code_objects:
        if code_object.object_name == class_name:
            for sub_code_object in code_object.code_objects:
                if sub_code_object.object_name == function_name:
                    return sub_code_object
    return None


class PycHandler(BaseHandler):
    def __init__(self, file_path):
        super().__init__(file_path)
        with open(file_path, 'rb') as f:
            self.data = f.read()

    def verify(self):
        # print(repr(self.data[:10])) # TODO: Make this work with all pyc versions
        return self.data[:4] == b'o\r\r\n'

    def handle(self):
        '''if not self.verify():
            pass
            raise ValueError('Invalid pyc file')'''

        # Disassemble the pyc file with pycdas executable in config.PYCDAS_PATH
        pycdas_path = config.PYCDAS_PATH
        if not os.path.exists(pycdas_path):
            raise FileNotFoundError('pycdas executable not found')
        logger.info(f'Converting pyc file to bytecode : {self.file_path}')
        bytecode_text = subprocess.check_output(
            [pycdas_path, self.file_path], stderr=subprocess.DEVNULL)

        # Split disassembled python code into functions using the PycCodeObject class
        bytecode_text = bytecode_text.decode().split('\n')
        file_as_code_object = PycCodeObject(bytecode_text[1:])

        # For optimization, now we need to try to disassemble the pyc back to source code using pycdc, and then only fix the functions that are not correctly disassembled
        # This is because pycdas does not always disassemble the code correctly
        pycdc_path = config.PYCDC_PATH
        if not os.path.exists(pycdc_path):
            raise FileNotFoundError('pycdc executable not found')
        logger.info(f'Converting pyc file to source code: {self.file_path}')
        sourcecode_text = subprocess.check_output(
            [pycdc_path, self.file_path], stderr=subprocess.DEVNULL)
        to_reconstruct = extract_broken_functions(sourcecode_text)
        to_reconstruct = to_reconstruct[::-1] # reverse the list to start reconstructing from the bottom of the file, reducing the need to shift line numbers in the future
        
        sourcecode_text_lines = sourcecode_text.split(b'\n')
        sourcecode_text_lines = convert_indent_to_spaces(sourcecode_text_lines)
        
        model = Model()
        for class_name, func_name, (start, end) in to_reconstruct:
            logger.info(
                f"Reconstructing function {func_name} in class {class_name}")
            code_obj = get_function_from_code_objects(
                file_as_code_object, class_name, func_name)
            if not code_obj:
                raise ValueError(
                    f"{self.file_path} : Function {func_name} in class {class_name} not found in code object")

            # in an effort to reduce token count, we will remove as much whitespace as possible from the bytecode
            lowest_indent = min([len(x) - len(x.lstrip()) for x in code_obj.disassembly])
            bytecode = '\n'.join([x[lowest_indent:] for x in code_obj.disassembly])

            prompt = PROMPT_TEMPLATE.format(code=bytecode, func_name=func_name)
            converted_sourcecode = model.generate(prompt)

            # print(converted_sourcecode)
            
            # TODO cleanup, indent, and inject into pycdc result sourcecode_text
            converted_sourcecode = converted_sourcecode.split('```')[1].strip('python').strip()
            converted_sourcecode = converted_sourcecode.split('\n')
            converted_sourcecode = convert_indent_to_spaces(converted_sourcecode)

            # inject the converted source code into the source code text
            sourcecode_text_lines = sourcecode_text_lines[:start] + converted_sourcecode + sourcecode_text_lines[end+1:]
        
        sourcecode_text_lines_same_format = []
        for line in sourcecode_text_lines:
            if isinstance(line,bytes):
                sourcecode_text_lines_same_format.append(line.decode())
            else:
                sourcecode_text_lines_same_format.append(line)

        # convert to string and return
        return '\n'.join(sourcecode_text_lines_same_format)
