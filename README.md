# Introduction to Galactica model(BIPT Deep Learning Class on LLMs)


# CLI interface for GALACTICA
A simple cli for the [GALACTICA](https://github.com/paperswithcode/galai) LLM. 

## Installation 

https://github.com/FlagAI-Open/FlagAI

- To install FlagAI with pip:
```shell
pip install -U flagai
```

or
```bash
pipx install git+https://github.com/tengda89757-edu/flagai_galactica_cli.git
```
## Usage
After installing the CLI interface with pipx you can use it from anywhere via your commandline:
```bash
galai_cli "Please write a abstract about the computer vision."   
```

## Features

```
Positional arguments:
  prompt                Prompt for the language model. Special tokens are used to nudge the 
                        language model to perform specific tasks, they include: 
                        [START_REF]      : insert a Reference. 
                        <work>           : reason about a question posed in the prompt. 
                        TLDR:            : produce a TLDR summary of the prompt. 
                        [START_I_SMILES] : generate a molecule/molecules.
                        [START_AMINO]    : generate a protein annotation.


```
See https://github.com/paperswithcode/galai and galactica.org for more information on the GALACTICA model.