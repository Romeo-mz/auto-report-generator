from transformers import pipeline

class GPT2:
    def __init__(self):
        self.generator = pipeline('text-generation', model='gpt2')

    def generate(self, prompt):
        return self.generator(prompt, max_length=100, num_return_sequences=1, do_sample=True)[0]['generated_text']
    
    def generate_multiple(self, prompt, num_return_sequences=5):
        return self.generator(prompt, max_length=100, num_return_sequences=num_return_sequences)
    
    def prompt(self, prompt, context):
        return self.answer_question(prompt, context)['answer']
    
    def answer_question(self, question, context):
        return self.question_answerer(question = question, context = context)
