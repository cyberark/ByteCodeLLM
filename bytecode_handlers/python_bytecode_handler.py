from utilities.base_handler import BaseHandler


TEMPLATE = """
Given the following dissasembled python code of a function {function_name}:
{disassembled_code}

Convert it back to python source code, only return the function {function_name} and its code.

Reconstructed code:

"""
class PyBytecodeHandler(BaseHandler):

    @staticmethod
    def handle(function_name, bytecode_in_a_string, model):

        print("Handling python bytecode for function: ", function_name)
        question = TEMPLATE.format(function_name=function_name, disassembled_code=bytecode_in_a_string)
        # USAGE: Send a string with a full prompt with prompt engineering that includes the function name and the disassembled code
        # Expected output: python code
        python_code = model.generate_local(question)
        print(python_code)
        return python_code
