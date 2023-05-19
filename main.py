from pdf_processing.pdf_extractor import *

def main():
    pdf_file_path = 'input/enonce_TP.pdf'  # Chemin vers le fichier PDF à traiter
    extracted_text = extract_text_from_pdf(pdf_file_path)
    # print(extracted_text)
    cr = transform_output_to_report(extracted_text)

    print(cr)
if __name__ == '__main__':
    main()