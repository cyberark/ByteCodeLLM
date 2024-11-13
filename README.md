# ByteCodeLLM

![License](https://img.shields.io/github/license/cyberark/ByteCodeLLM) ![Issues](https://img.shields.io/github/issues/cyberark/ByteCodeLLM) ![Stars](https://img.shields.io/github/stars/cyberark/ByteCodeLLM)

A comprehensive framework for decompiling intermediate language based files back to source code using local LLM for both efficiency and privacy.

Currently supported languages:
* Python 3 (ALL VERSIONS INCLUDING AND UP TO 3.13)
---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Installation
To install the project start by compiling the pycdc project, to do so please follow the compilation instructions on [https://github.com/zrax/pycdc](https://github.com/zrax/pycdc)

After compiling the project you should have both `pycdc` and `pycdas` executables ready, store those paths to the side as it will be needed for the configuration

Then we can setup the project by cloning the repository
```
git clone https://github.com/cyberark/ByteCodeLLM
```

Change the configuration inside the file `config.py` to suit your needs, see [Configuration](#configuration) for more in depth information.

Make sure to point the `PYCDAS_PATH` and `PYCDC_PATH` variables to where you have them stored
## Usage
After configuration, you can run the project by running the main file `ByteCodeLLM.py`

```
python ByeCodeLLM.py [-h] [--path PATH] [--output OUTPUT] [--type {exe,pyc,folder,py_bytecode}] [--llm LLM] [--llm-args LLM_ARGS]

ByeCodeLLM

options:
  -h, --help            show this help message and exit
  --path PATH           Path to the file or directory to convert
  --output OUTPUT       Output path
  --type {exe,pyc,folder,py_bytecode}
                        Type of the input
  --llm LLM             Name or path to the LLM file by default goes to one of the pretrained LLM's included
  --llm-args LLM_ARGS   Arguments to pass to the LLM
```

If you know the input file type specify it using the `--type` argument, currently supported types:
* PYC
* Folder of PYC files (TBA)
* EXE (TBA)

And you can change the output folder / file through the `--output` argument



## Features
### Python 3
This tool currently supports `.pyc` files (compiled Python), with future plans to extend support to a full pipeline from `.exe` to `.py`.

For handling `.pyc` files, we utilize `pycdc`, an open-source tool designed to extract bytecode and attempt source code reconstruction. Unlike Python’s built-in `dis` module, `pycdc` works across all Python versions without depending on a specific version installed on your machine.

#### Process Overview

1. **Decompilation**: We start by decompiling the `.pyc` file using `pycdc` for an incomplete source code and `pycdas` for a complete bytecode.
2. **Identifying Incomplete Functions**: Any functions that weren’t fully decompiled are marked with the comment `# WARNING: Decompyle incomplete`.
3. **Bytecode Recovery**: For these incomplete functions, we retrieve the corresponding bytecode.
4. **LLM-Based Source Conversion**: Using a finetuned language model (LLM) hosted locally on your machine translates the bytecode back into source code.
5. **Integration**: The generated source code is then injected into the initial output from `pycdc`, creating a more complete final code.

This approach combines the strengths of `pycdc` and `pycdas` parsing capabilities and version-independent approach with advanced LLMs to enhance decompilation quality and make up for the gap between the newest versiosn of python and the lack of capability in `pycdc` to support them.



## Configuration
In the `config.py` file you will see pre filled configurations for utilizing LLM modules in one of 3 ways - 
1. HuggingFace - for running models stored on huggingface
2. Local - for running models you might have downloaded or trained yourself
3. Ollama - for running LLM models through the flexible Ollama application, allowing both local and remote execution

Additionally, this file contains the paths to utility files like pycdc, point those paths to the corresponding files:
```python
# Utility executables
PYCDC_PATH = '/usr/local/bin/pycdc' #  Path to PYCDC file
PYCDAS_PATH = '/usr/local/bin/pycdas' # Path to PYCDAS file

```

## Contributing
Currently we are not seeking for active contribution and maintainers, please use the issues feature to open feature requests and bug reports

## License
ByteCodeLLM is licensed under the TBD license, read more about it in the LICENSE file

A list of all assets used in the project and their respective license
External tools:
* pyinstxtractor - [GNU 3.0](https://github.com/extremecoders-re/pyinstxtractor/blob/master/LICENSE)
* pycdc - [GPL 3.0](https://github.com/zrax/pycdc/blob/master/LICENSE)

External Python libraries:
* llama_cpp - [MIT](https://github.com/ggerganov/llama.cpp/blob/master/LICENSE)
* huggingface_hub - [Apache 2.0](https://github.com/huggingface/huggingface_hub/blob/main/LICENSE)
* requests - [Apache 2.0](https://github.com/psf/requests/blob/main/LICENSE)

Suggested LLM models:
* bartowski/gemma-2-9b-it-GGUF - [Gemma](https://ai.google.dev/gemma/terms)
* ByteCodeLLM - TBD

Used datasets to train:
* TDB

Used examples for PYC come from empyrean under the license of [MIT](https://github.com/addi00000/empyrean/blob/main/LICENSE.md)

## Contact
Feel free to contact us via github issues if there are any feature requests or issues in the project
And contact us through email via david.el@cyberark.com and amir.landau@cyberark.com