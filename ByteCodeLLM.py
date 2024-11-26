import argparse
import os
import sys
from file_extractors import PycHandler
import time
import logging
# setup logging to print to console
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DIRECTORY = os.path.abspath(os.getcwd())

def is_safe_path(base_path, user_path):
    # Resolve absolute paths
    absolute_base = os.path.abspath(base_path)
    absolute_user = os.path.abspath(user_path)
    # Ensure the user path is within the base path
    return os.path.commonpath([absolute_base, absolute_user]) == absolute_base

def main():
    start = time.time()
    # initialize all the built in llm options
    llm_options = ['auto']
    if os.path.exists('llm'):
        llm_options += os.listdir('llm')
        # TODO: check this works down the line, this is only a placeholder

    parser = argparse.ArgumentParser(description='ByeCodeLLM')
    parser.add_argument('--path', type=str,
                        help='Path to the file or directory to convert')
    parser.add_argument('--output', type=str,
                        help='Output path', default='output')
    parser.add_argument('--type', type=str, help='Type of the input',
                        choices=['exe', 'pyc', 'folder', 'py_bytecode'], default='pyc')
    parser.add_argument(
        '--llm', help='Name or path to the LLM file by default goes to one of the pretrained LLM\'s included', default='auto')
    parser.add_argument(
        '--llm-args', help='Arguments to pass to the LLM', default="")

    args = parser.parse_args()
    
    if args.llm not in llm_options:
        print('Invalid LLM option')
        sys.exit(1)

    if not os.path.exists(args.path):
       raise ValueError(f"Error: The provided path '{args.path}' does not exist.")
    
    if args.type == 'pyc':
    # Ensure the input path is valid
        if not os.path.exists(args.path) or not is_safe_path(BASE_DIRECTORY, args.path):
            raise ValueError(f"Error: Invalid or unsafe path '{args.path}'")

        res = PycHandler(args.path).handle()

        # Ensure the output path is safe
        if not is_safe_path(BASE_DIRECTORY, args.output):
            raise ValueError(f"Error: Unsafe output path '{args.output}'")

        with open(args.output, 'w') as f:
            f.write(res)

    time_in_seconds = time.time() - start
    import datetime
    print(f"Time taken: {str(datetime.timedelta(seconds=time_in_seconds))}")


if __name__ == '__main__':
    main()
