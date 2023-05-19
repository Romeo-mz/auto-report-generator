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

        # Vérifier si la ligne est un titre ou une question
        if re.match(r"^\d+\. .*", line):
            section = line.split(". ", 1)[1]
            line = ""
        elif line.startswith("a.") or re.match(r"^\d+\..*", line):
            section = re.sub(r"^\w+\.\s*", "", line)
            line = ""

        # Ajouter la ligne au compte rendu uniquement si une section est déjà présente et la ligne n'est pas vide
        if section and line and section not in section_dict:
            report += f"{section} : {line}\n\n"
            section_dict[section] = True

    return report.strip()
