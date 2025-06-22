
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./vector_store")
PDF_UPLOAD_PATH = os.getenv("PDF_UPLOAD_PATH", "../data")
