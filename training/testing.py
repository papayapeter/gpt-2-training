import os
from aitextgen import aitextgen

model_directory = 'model'

ai = aitextgen(model_folder=model_directory, to_gpu=True)

prompt = 'Dear Zeno,\nI don\'t think'

response = ai.generate_one(
    prompt=prompt,
    min_length=
    64,  # The minimum length of the generated text: if the text is shorter than this value after cleanup, aitextgen will generate another one.
    max_length=
    256,  # Number of tokens to generate (default 256, you can generate up to 1024 tokens with GPT-2 and 2048 with GPT Neo)
    temperature=
    1.0,  # The higher the temperature, the crazier the text (default 0.7, recommended to keep between 0.7 and 1.0)
    top_k=
    0,  # Limits the generated guesses to the top k guesses (default 0 which disables the behavior; if the generated output is super crazy, you may want to set top_k=40)
    top_p=
    0.9,  # Nucleus sampling: limits the generated guesses to a cumulative probability. (gets good results on a dataset with top_p=0.9)
    seed=0)

print(response)