# gpt-2-training

for dataset parsing, dataset preperation & finetuning gpt-2 to generate conversations about ai, cybernetics, control and ghosts

### directions

1. parse `.eml` mails with `mail_parsing/parse_editing.py`
2. manually add turn them into a chat like:
   - person1> message text.
   - person2> message text.
   - ...
3. finetune gpt-2/neo model with the chat using the notebook `aitextgen_finetune.ipynb`

## research links

- [model finetuning](https://www.philschmid.de/fine-tune-a-non-english-gpt-2-model-with-huggingface)
- [hugginface model database](https://huggingface.co/models)
- [hugginface transformer docs](https://huggingface.co/transformers/)
- [finetuning with aitextgen](https://github.com/minimaxir/aitextgen) [(docs)](https://docs.aitextgen.io/)

### setup

1. to create the envorinment: `conda env create -f environment.yml`
2. activate the enviroment: `conda activate transformers`
3. changes to the environment can be saved with: `conda env export --no-builds | grep -v "prefix" > environment.yml`
