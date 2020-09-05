from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# the prompt to add the generated text to
prompt = "Hallo mein Name ist"

# model und tokenizer (https://huggingface.co/models)
model_name = 'anonymous-german-nlp/german-gpt2'
tokenizer_name = 'anonymous-german-nlp/german-gpt2'

# parameters for generation
parameters = {
    'length': 128,
    'temperature': 1.0,  # default: 1.0
    'top_k': 0,  # default: 0
    'top_p': 0.9,  # default: 0.9
    'repetition_penalty': 1.0,  # default: 1.0 (primarily useful for CTRL model)
    'num_return_sequences': 1,  # default: 1
    'stop_token': None,  # character or None
    'seed': 0
}

# device to be used (cuda gpu or cpu)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# tokenizer and model objects
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained('anonymous-german-nlp/german-gpt2')

model.to(device)

# encode prompt to tokens
encoded_prompt = tokenizer.encode(prompt, return_tensors="pt")
encoded_prompt = encoded_prompt.to(device)

# if the encoded prompt is empty, set the model input to None
if encoded_prompt.size()[-1] == 0:
    input_tokens = None
else:
    input_tokens = encoded_prompt

# generate output sequence with parameters
output_sequences = model.generate(
    input_ids=input_tokens,
    max_length=parameters['length'] + len(encoded_prompt[0]),
    temperature=parameters['temperature'],
    top_k=parameters['top_k'],
    top_p=parameters['top_p'],
    repetition_penalty=parameters['repetition_penalty'],
    do_sample=True,
    num_return_sequences=parameters['num_return_sequences'],
)

# remove the batch dimension when returning multiple sequences
if len(output_sequences.shape) > 2:
    output_sequences.squeeze_()

# decode sequence(s) from tokens to text
generated_sequences = []

for generated_sequence_id, generated_sequence in enumerate(output_sequences):
    print("=== GENERATED SEQUENCE {} ===".format(generated_sequence_id + 1))
    generated_sequence = generated_sequence.tolist()

    # decode text
    text = tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=True)

    # remove all text after the stop token
    text = text[: text.find(parameters['stop_token']) if not parameters['stop_token'] is None else None]

    # add the prompt at the beginning of the sequence. Remove the excess text that was used for pre-processing
    total_sequence = (
        prompt + text[len(tokenizer.decode(encoded_prompt[0], clean_up_tokenization_spaces=True)) :]
    )

    generated_sequences.append(total_sequence)

print(generated_sequences)
