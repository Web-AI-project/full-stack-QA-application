
import PyPDF2

def process_pdf(path):
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    return chunks
