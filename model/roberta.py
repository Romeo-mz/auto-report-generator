from transformers import pipeline

class RobertaSquad2:
    def __init__(self):
        self.question_answerer = pipeline('question-answering', model='deepset/roberta-base-squad2', tokenizer='deepset/roberta-base-squad2')

    def answer_question(self, context, question):
        return self.question_answerer(question=question, context=context)

# Exemple d'utilisation
context = "Tu es un étudiant en informatique qui réponds à un énoncé de TP image en python. Tu dois répondre à la question suivante:"
question = "Coder un système d’affichage niveau de gris pour la luminosité et la saturation et couleur pour la teinte"

roberta_squad2 = RobertaSquad2()
answer = roberta_squad2.answer_question(context, question)

print("Question:", question)
print("Réponse:", answer['answer'])
print("Score de confiance:", answer['score'])
