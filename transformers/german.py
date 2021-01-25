from transformers import pipeline

pipe = pipeline('text-generation', model="dbmdz/german-gpt2",
                tokenizer="dbmdz/german-gpt2")

text = pipe("Der Sinn des Lebens ist es", max_length=100)[0]["generated_text"]

print(text)
