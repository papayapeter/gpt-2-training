import os
from aitextgen import aitextgen

ai = aitextgen(model_folder=os.path.join('models', 'german_2000'), to_gpu=True)

prompt = 'Lieber Zeno,\nich glaube nicht'

response = ai.generate_one(
    prompt=prompt, max_length=256, temperature=1.0, top_p=0.7
    )

print(response)