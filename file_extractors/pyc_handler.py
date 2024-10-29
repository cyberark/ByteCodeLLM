from utilities.base_handler import BaseHandler
from bytecode_handlers.python_bytecode_handler import PyBytecodeHandler
from utilities.model import Model
from utilities.util_functions import reduce_indent_by_one, find_closest_match, increase_indent_by_one, convert_indent_to_spaces
import subprocess
import os
import config
from file_extractors.model_return_handler import ModelReturnHandler


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

        object_name_index = find_closest_match(lines,0,'Object Name:')
        self.object_name = lines[object_name_index].split(':')[1].strip()

        names_index = find_closest_match(lines,2,'[Names]')
        names_end_index = find_closest_match(lines,names_index,'[Var Names]')
        self.names = lines[names_index+1:names_end_index]

        var_names_index = find_closest_match(lines,names_end_index,'[Var Names]')
        var_names_end_index = find_closest_match(lines,var_names_index,'[Free Vars]')
        self.var_names = lines[var_names_index+1:var_names_end_index]

        free_vars_index = find_closest_match(lines,var_names_end_index,'[Free Vars]')
        free_vars_end_index = find_closest_match(lines,free_vars_index,'[Cell Vars]')
        self.free_vars = lines[free_vars_index+1:free_vars_end_index]

        cell_vars_index = find_closest_match(lines,free_vars_end_index,'[Cell Vars]')
        cell_vars_end_index = find_closest_match(lines,cell_vars_index,'[Constants]')
        self.cell_vars = lines[cell_vars_index+1:cell_vars_end_index]

        constants_index = find_closest_match(lines,cell_vars_end_index,'[Constants]')
        constants_end_index = find_closest_match(lines,constants_index,'[Disassembly]')
        constants = lines[constants_index+1:constants_end_index]

        disassembly_index = find_closest_match(lines,constants_end_index,'[Disassembly]')
        disassembly_end_index = len(lines)
        self.disassembly = lines[disassembly_index+1:disassembly_end_index]

        self.names = [x.strip().strip("'") for x in self.names if x.strip()]
        self.var_names = [x.strip().strip("'") for x in self.var_names if x.strip()]
        self.free_vars = [x.strip().strip("'") for x in self.free_vars if x.strip()]
        self.cell_vars = [x.strip().strip("'") for x in self.cell_vars if x.strip()]
        self.disassembly = [x.strip() for x in self.disassembly if x.strip()]

        # extract all code objects from constants
        constants = reduce_indent_by_one(constants)
        more_code_to_extract = find_closest_match(constants,0,'[Code]')
        while more_code_to_extract:
            code_object_start = more_code_to_extract + 1
            code_object_end = find_closest_match(constants,code_object_start,"'")
            more_code_to_extract = find_closest_match(constants,more_code_to_extract+1,'[Code]')
            code_object = constants[code_object_start:code_object_end]
            self.code_objects.append(PycCodeObject(code_object))

    def __str__(self, level=0):
        res = f"{'    '*(level+1)}Object Name: {self.object_name}\n"
        for code_object in self.code_objects:
            res += code_object.__str__(level=level+1)
        return res
    
    def __repr__(self):
        return self.__str__()
    
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
        print('Disassembling pyc file')
        disassembled_code = subprocess.check_output([pycdas_path, self.file_path])
        print('Disassembled pyc file')
        # print(disassembled_code)

        # Split disassembled python code into functions using the PycCodeObject class
        disassembled_code = disassembled_code.decode().split('\n')
        file_as_code_object = PycCodeObject(disassembled_code[1:])
        
        # In a recursive manner, convert the disassembled code to python source code, starting from the lowest level code objects
        # For each code object, convert using the PyBytecodeHandler class and fix indentation based on the level

        bytecode_handler = PyBytecodeHandler
        model_return_hundler = ModelReturnHandler
        model = Model('mistral:latest')
        def convert_code_object_to_python(code_object, level=0):
            python_code = ''
            for code_object in code_object.code_objects:
                python_code += convert_code_object_to_python(code_object, level=level+1)
            if code_object.disassembly:
                function_name = code_object.object_name
                bytecode_in_a_string = '\n'.join(code_object.disassembly)
                res = bytecode_handler.handle(function_name, bytecode_in_a_string,model=model)
                res = model_return_hundler.handle(function_name,res,model=model)
                python_code += f"\n{res}"
            
            return python_code
        
        python_code = convert_code_object_to_python(file_as_code_object)

        return python_code
