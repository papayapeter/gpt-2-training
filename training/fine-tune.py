import os
from aitextgen import aitextgen

os.environ["TOKENIZERS_PARALLELISM"] = "false"
ai = aitextgen(tf_gpt2="124M", to_gpu=True)

file_name = os.path.join('parsed', 'parsed.txt')

output_dir = 'model'

ai.train(file_name,
         output_dir=output_dir,
         line_by_line=False,
         from_cache=False,
         num_steps=2000,
         generate_every=500,
         save_every=500,
         # save_gdrive=True,
         learning_rate=1e-3,
         fp16=False,
         batch_size=1, 
         )