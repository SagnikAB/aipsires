import PyPDF2

def extract_text(path):
    text = ""
    if path.endswith(".pdf"):
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
    else:
        with open(path, "r", errors="ignore") as f:
            text = f.read()
    return text.lower()
