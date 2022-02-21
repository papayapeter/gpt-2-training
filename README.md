# ghosts-of-data

research for finetraining gpt-2 to generate monologues/dialogues about ghosts

## research links

- [model finetuning](https://www.philschmid.de/fine-tune-a-non-english-gpt-2-model-with-huggingface)
- [hugginface model database](https://huggingface.co/models)
- [hugginface transformer docs](https://huggingface.co/transformers/)
- [finetuning with aitextgen](https://github.com/minimaxir/aitextgen) [or](https://docs.aitextgen.io/)
- [conda cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

## info

- conda environment is needed. requirements file is provided

## used packages

### conda
- python 3.8.10
- ipykernel
- yapf
- pandas
- pytorch (with cuda 10.2)
- tensorflow
- (huggingface) transformers


### pip
- aitextgen

### setup

1. to create the envorinment: `conda env create -f transformers.yml`