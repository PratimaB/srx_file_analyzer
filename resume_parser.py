# resume_parser.py
import fitz  # PyMuPDF

def extract_resume_text(file) -> str:
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()
