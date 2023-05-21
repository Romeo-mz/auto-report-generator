from transformers import pipeline

class GPT2:
    def __init__(self):
        self.generator = pipeline('text-generation', model='gpt2')

    def generate(self, prompt):
        return self.generator(prompt, max_length=700, num_return_sequences=1)[0]['generated_text']
    
    def generate_multiple(self, prompt, num_return_sequences=5):
        return self.generator(prompt, max_length=700, num_return_sequences=num_return_sequences)
    
    def prompt(self, prompt):
        return self.generate(prompt)