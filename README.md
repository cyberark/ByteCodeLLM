![ByteCodeLLMBackgroung](https://github.com/cyberark/ByteCodeLLM/blob/main/Pic_ByteCodeLLM.png)

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
### Prerequisite: Compile pycdc and pycdas
Follow the instructions [here](https://github.com/zrax/pycdc) to compile the `pycdc` and `pycdas` executables.

Once compiled, note their paths for later configuration (e.g., `/usr/local/bin/pycdc`).

**Then we can setup the project by cloning the repository:**
```
git clone https://github.com/cyberark/ByteCodeLLM
```

Change the configuration inside the file `config.py` to suit your needs, see [Configuration](#configuration) for more in depth information.

**Make sure to point the `PYCDAS_PATH` and `PYCDC_PATH` variables to where you have them stored.**
## Usage
After configuration, you can run the project by running the main file `ByteCodeLLM.py`

```
python ByeCodeLLM.py [-h] [--path PATH] [--output OUTPUT] [--type {exe,pyc,folder,py_bytecode}] [--llm LLM] [--llm-args LLM_ARGS]

USAGE EXAMPLE:
python ByteCodeLLM.py --path ./examples/test.pyc --type pyc --output ./output

# This command decompiles test.pyc to Python source and saves the output in the ./output folder

ByteCodeLLM

options:
  -h, --help            show this help message and exit
  --path PATH           Path to the file or directory to convert
  --output OUTPUT       Output path
  --type {exe,pyc,folder,py_bytecode}
                        Type of the input
  --llm LLM             Name or path to the LLM file by default goes to one of the pretrained LLM's included  - default will download Gemma 2 9B 
  --llm-args LLM_ARGS   Arguments to pass to the LLM
```

If you know the input file type specify it using the `--type` argument, currently supported types:
* PYC
* Folder of PYC files (TBA)
* EXE (TBA)

And you can change the output folder / file through the `--output` argument

## Compiled Versions
Pre-compiled versions (ELF/EXE) of ByteCodeLLM are available for convenience. 
You can download the latest release directly from the [GitHub Releases](https://github.com/cyberark/ByteCodeLLM/releases) page.

## Compiling From Source
If you prefer to compile ByteCodeLLM from the source code, follow these steps:
Refer to the instructions on the [GitHub Releases](https://github.com/cyberark/ByteCodeLLM/releases) page.

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

This approach combines the strengths of `pycdc` and `pycdas` parsing capabilities and version-independent approach with advanced LLMs to enhance decompilation quality and make up for the gap between the newest versions of python and the lack of capability in `pycdc` to support them.



## Configuration
In the `config.py` file you will see pre filled configurations for utilizing LLM modules in one of three ways - 
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
ByteCodeLLM is licensed under the GNU General Public License v3.0, read more about it in the LICENSE file

## Third Parties
A list of all third-party libraries and assets used in the project and their respective licenses can be found in the NOTICES file.

Suggested LLM models:
* bartowski/gemma-2-9b-it-GGUF ((https://huggingface.co/bartowski/gemma-2-9b-it-GGUF) - this is the LLM model suggested by default . Please note that this is not an integral part of ByteCodeLLM’s code and can be replaced with other models. 

## External Tools and Libraries <br />
Pyinstxtractor (https://github.com/extremecoders-re/pyinstxtractor) - a recommended component for extracting PYC. This component is not included in ByteCodeLLM’s code. 

## Contact
Feel free to contact us via github issues if there are any feature requests or issues in the project
And contact us through linkedin:<br />
[David El](linkedin.com/in/david-el/) and [Amir Landau](linkedin.com/in/amirlandau)
