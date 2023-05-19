from pdf_processing.pdf_extractor import extract_text_from_pdf

def main():
    pdf_file_path = 'input/enonce_TP.pdf'  # Chemin vers le fichier PDF à traiter
    extracted_text = extract_text_from_pdf(pdf_file_path)
    print(extracted_text)

if __name__ == '__main__':
    main()