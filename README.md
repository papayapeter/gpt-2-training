# ghosts-of-data

for dataset parsing, dataset preperation & finetuning gpt-2 to generate conversations about ai, cybernetics, control and ghosts
additionaly parsing, dataset preperation & interpolation generation with stylegan2 to create videos of the conversation partners

## global resources

- [conda cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)
- [rough direction where to fientune gans/transformers with runway ml](https://runwayml.com/training/) (in case gans turn out to be to complicated/costly)

# gpt-2 dialogues

### directions

1. parse `.eml` mails with `parse-mails.py` (creates files by senders. splits mails by paragraph to create smaller submails)
2. possibly concat the mails of different senders to one text file with `concat-mails.py`. manual collection/curation/concating might be needed instead.
3. finetune gpt-2/neo model with the parsed mails using the notebook `aitextgen_finetune.ipynb` locally or on google colab (found in the colab directory)

## research links

- [model finetuning](https://www.philschmid.de/fine-tune-a-non-english-gpt-2-model-with-huggingface)
- [hugginface model database](https://huggingface.co/models)
- [hugginface transformer docs](https://huggingface.co/transformers/)
- [finetuning with aitextgen](https://github.com/minimaxir/aitextgen) [(docs)](https://docs.aitextgen.io/)

## used packages

#### conda

- python 3.8: `conda create --name transformers python=3.8`
- ipykernel/yapf/pandas: `conda install ipykernel yapf pandas`
- pytorch (with cuda 11.3): `conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch`
- tensorflow: `conda install tensorflow`
- (huggingface) transformers: `conda install -c huggingface transformers`

#### pip

- aitextgen: `pip3 install aitextgen`

### setup

1. to create the envorinment: `conda env create -f environment.yml`
2. activate the enviroment: `conda activate transformers`
3. changes to the environment can be saved with: `conda env export --no-builds | grep -v "prefix" > environment.yml`
