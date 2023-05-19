import PyPDF2
import re 

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

def transform_output_to_report(output):
    report = ""
    lines = output.split("\n")
    section = ""
    section_dict = {}


    for line in lines:
        line = line.strip()

        # Ajouter la ligne au compte rendu si elle n'est pas vide
        if line:
            report += f"{line}\n\n"

    return report.strip()

