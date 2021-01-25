from transformers import pipeline

pipe = pipeline('text-generation', model="gpt2-large",
                tokenizer="gpt2-large")

text = pipe("The point of life is", max_length=100)[0]["generated_text"]

print(text)
