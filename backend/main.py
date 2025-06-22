
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services.pdf_processor import process_pdf
from services.vector_store import store_vectors, query_vectors
from services.rag_pipeline import generate_answer
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/upload")
async def upload_pdf(file: UploadFile = File(...)):
    content = await file.read()
    filename = file.filename
    save_path = os.path.join("../data", filename)
    with open(save_path, "wb") as f:
        f.write(content)
    chunks = process_pdf(save_path)
    store_vectors(chunks)
    return {"message": "PDF uploaded and processed."}

@app.get("/api/documents")
def get_documents():
    return {"documents": ["FinancialStatement_2025_I_AADIpdf.pdf"]}

@app.post("/api/chat")
def chat(query: dict):
    question = query.get("question", "")
    if not question:
        raise HTTPException(status_code=400, detail="Question required")
    results = query_vectors(question)
    answer = generate_answer(question, results)
    return {"answer": answer, "sources": results}
