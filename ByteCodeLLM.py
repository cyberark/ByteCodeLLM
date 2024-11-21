import argparse
import os
import sys
from file_extractors import PycHandler
import time
import logging
# setup logging to print to console
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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

    if args.type == 'pyc':
        res = PycHandler(args.path).handle()
    with open(args.output, 'w') as f:
        f.write(res)
    # print(res)

    time_in_seconds = time.time() - start
    import datetime
    print(f"Time taken: {str(datetime.timedelta(seconds=time_in_seconds))}")


if __name__ == '__main__':
    main()
