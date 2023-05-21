from pdf_processing.pdf_extractor import *
from model.roberta import *

def main():
    pdf_file_path = 'input/enonce_TP.pdf'  # Chemin vers le fichier PDF à traiter
    extracted_text = extract_text_from_pdf(pdf_file_path)
    # print(extracted_text)
    
    cr = transform_output_to_report(extracted_text)
    
    # gpt2 = GPT2()

    # print(gpt2.answer_question(" Ecrit un programme qui affiche 'Hello World" , "Bonjour, tu dois répondre à la manière d'un etudiant en informatique à la question suivante: "))

    # Exemple d'utilisation
    context = "Tu es un étudiant en informatique qui réponds à un énoncé de TP image en python. Tu dois répondre à la question suivante:"
    question = "Coder un système d’affichage niveau de gris pour la luminosité et la saturation et couleur pour la teinte"

    roberta_squad2 = RobertaSquad2()
    answer = roberta_squad2.prompt(context, question)

    print("Question:", question)
    print("Réponse:", answer)
    

if __name__ == '__main__':
    main()