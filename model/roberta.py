from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline


class RobertaSquad2:
    def __init__(self):
        self.model_name = "deepset/roberta-base-squad2"

        self.model = AutoModelForQuestionAnswering.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.question_answerer = pipeline('question-answering', model=self.model, tokenizer=self.tokenizer)

    def answer_question(self, question, context):
        nlp = pipeline('question-answering', model=self.model_name, tokenizer=self.tokenizer)
        QA_input = {
            'question': question,
            'context': context
        }
        res = nlp(QA_input)

        return res
    
    def prompt(self, prompt, context):
        return self.answer_question(prompt, context)


