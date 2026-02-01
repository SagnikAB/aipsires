import PyPDF2
import docx
import spacy

nlp = spacy.load("en_core_web_sm")

SKILL_DB = ["python", "java", "machine learning", "sql", "html", "css"]

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        text = ""
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text()
        return text

    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])

    return ""

def extract_skills(text):
    text = text.lower()
    found = []
    for skill in SKILL_DB:
        if skill in text:
            found.append(skill)
    return found
