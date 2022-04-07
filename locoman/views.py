from docx import Document
import docx

def readingDocuments(filename):
    doc = Document(filename)

    doc_text = []

    for paragraph in doc:
        doc_text.append(paragraph.text)

    return '\n' .join(doc_text)