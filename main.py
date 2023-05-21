from pdf_processing.pdf_extractor import *
from model.gpt2 import *

def main():
    pdf_file_path = 'input/enonce_TP.pdf'  # Chemin vers le fichier PDF à traiter
    extracted_text = extract_text_from_pdf(pdf_file_path)
    # print(extracted_text)
    
    cr = transform_output_to_report(extracted_text)
    
    gpt2 = GPT2()

    print(gpt2.prompt("Bonjour, je suis un robot. Je suis capable de générer des rapports de TP à partir d'un énoncé."))
if __name__ == '__main__':
    main()