from utilities.base_handler import BaseHandler
from utilities.util_functions import is_valid_json, convert_indent_to_spaces, increase_indent_by_one
import config


TEMPLATE = """
Given the following dissasembled python code of a function {function_name}:
{disassembled_code}

Convert it back to python source code, only return the function {function_name} and its code.

Reconstructed code:

"""
class ModelReturnHandler(BaseHandler):

    @staticmethod
    def handle(function_name, res ,model):
        print("Handling model return for function: ", function_name)
        if isinstance(res, dict):
            res = res["choices"][0]["text"]
        else:
            res = res.split('\n')
            res = convert_indent_to_spaces(res)
            res = increase_indent_by_one(res)
            res = '\n'.join(res)
        return res

