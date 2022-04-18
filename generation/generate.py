import os
import time
from aitextgen import aitextgen

# ai = aitextgen(model_folder=os.path.join('models', 'german_2000'), to_gpu=True)
ai = aitextgen(model='EleutherAI/gpt-neo-125M')

prompt = 'I can\'t believe'

start = time.time()
response = ai.generate_one(
    prompt=prompt, max_length=128, temperature=1.0, top_p=0.7
    )

print(response)
print(f'--- generation took {time.time() - start}s')