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
- tensorflow: `conda install tensorflow `
- (huggingface) transformers: `conda install -c huggingface transformers`

#### pip

- aitextgen: `pip3 install aitextgen`

### setup

1. to create the envorinment: `conda env create -f transformers.yml`
2. activate the enviroment: `conda activate transformers`
3. changes to the environment can be saved with: `conda env export --no-builds | grep -v "prefix" > transformers.yml` this should be used with caution though. after pip packages have been installed, no packages should be installed through conda anymore.

# stylegan2-pytorch portrait interpolations

### directions

1. install [cuda toolkit host](https://developer.nvidia.com/cuda-toolkit), [ninja](https://ninja-build.org/) & check if GCC >= 7.x
2. fork stylegan and clone with `git clone https://github.com/NVlabs/stylegan2-ada-pytorch`
3. parse videos with `parse-images.py`
4. train the model with `python train.py --outdir=~/training-runs --data=~/datasets/dataset.zip --gpus=1 --cfg=paper1024 --mirror=1 --resume=ffhq1024 --snap=10`

## research links

- [stylegan2-ada-pytorch repo](https://github.com/NVlabs/stylegan2-ada-pytorch)
- [stylegan fork by Derrick Schultz](https://github.com/dvschultz/stylegan2-ada-pytorch) (might be a good inspiration for interpolations)
- **[stylegan3](https://github.com/NVlabs/stylegan3) (possibly better/easier interpolations and easier install thanks to conda env yml. also more contemporary pytorch version and very good docs)**
- [traversing the latent space](https://amarsaini.github.io/Epoching-Blog/jupyter/2020/08/10/Latent-Space-Exploration-with-StyleGAN2.html)
- [extract frames from video with opencv](https://medium.com/@iKhushPatel/convert-video-to-images-images-to-video-using-opencv-python-db27a128a481)
- [crop to face with opencv](https://www.geeksforgeeks.org/cropping-faces-from-images-using-opencv-python/)

## used packages

#### conda

- python 3.7: `conda create --name stylegan python=3.7`
- pytorch 1.7 (with cuda 11.3): `conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=11.3 -c pytorch`
- yapf/requests/numpy/tqdm/ninja: `conda install yapf requests numpy tqdm ninja`
- imageio-ffmpeg: `conda install -c conda-forge imageio-ffmpeg==0.4.3`

#### pip

- pyspng: `pip3 install pyspng`

# stylegan portrait interpolations _(obsolete)_

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

- python 3.7: `conda create --name stylegan python=3.7`
- tensorflow-gpu: `conda install tensorflow-gpu==1.13.1 cudatoolkit=10.2`
- tensorboard: `conda install tensorboard`
- yapf/pillow/numpy/scipy/opencv/lmdb: `conda install yapf pillow numpy scipy opencv lmdb`
- moviepy: `conda install -c conda-forge moviepy`
