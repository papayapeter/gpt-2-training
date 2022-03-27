# ghosts-of-data

for finetuning gpt-2 to generate conversations about ai, cybernetics, control and ghosts
additionaly for finetuning stylegan (1 or 2) to create image interpolations of the conversation partners

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

- python 3.8.10: `conda create --name transformers python=3.8.10`
- ipykernel/yapf/pandas: `conda install ipykernel yapf pandas`
- pytorch (with cuda 11.3): `conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch`
- tensorflow: `conda install tensorflow `
- (huggingface) transformers: `conda install -c huggingface transformers`

#### pip

- aitextgen: `pip3 install aitextgen`

### setup

1. to create the envorinment: `conda env create -f transformers.yml`
2. activate the enviroment: `conda activate transformers`
3. changes to the environment can be saved with: `conda env export --no-builds | grep -v "prefix" > transformers.yml` this should be used with caution though. after pip packages have been installed, no packages should be installed through conda anymore.

# stylegan portrait interpolations

### directions

1. parse videos with `parse-images.py`
2. get `lazy` with `git clone https://github.com/nshepperd/lazy` and add it to the terminal
3. install tensorflow, activate environment & test tensorflow with `python3 -c "import tensorflow as tf; tf.enable_eager_execution(); \ print(tf.reduce_sum(tf.random_normal([1000, 1000])))"`
4. install the rest of the depencies
5. clone stylegan with `git clone https://github.com/NVlabs/stylegan.git` (consider forking it first to apply "latest"-patch and others permanently)
6. train the model with `lazy python3 ...`

## research links

- [overview on how to finetune stylegans for painting ganeration](https://towardsdatascience.com/how-i-built-9-gans-an-ai-generated-art-gallery-app-part-1-277b24718e2)
- [indepth tutorial on how to finetune stylegans for manga portrait generation](https://www.gwern.net/Faces#interpolations)
- [extract frames from video with opencv](https://medium.com/@iKhushPatel/convert-video-to-images-images-to-video-using-opencv-python-db27a128a481)
- [crop to face with opencv](https://www.geeksforgeeks.org/cropping-faces-from-images-using-opencv-python/)

## used packages

#### conda

- python 3.8.10: `conda create --name stylegan python=3.8.10`
- yapf: `conda install yapf`
- tensorflow-gpu: `conda install tensorflow-gpu==1.13.1 cudatoolkit=10.2`
- tensorboard: `conda install tensorboard`
- pillow/numpy/scipy/opencv/lmdb: `conda install pillow scipy opencv lmdb`
- moviepy: `conda install -c conda-forge moviepy `

#### pip

- aitextgen: `pip3 install aitextgen`
