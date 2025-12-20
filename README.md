# Full Stack Q&A Application

A full-stack **Question & Answer (Q&A)** application that lets users submit questions, retrieves answers using an AI/ML-powered backend, and displays responses in an intuitive frontend UI.

##  Built with:
- **Next.js & React** (frontend)
- **FastAPI & Python** (backend)
- **OpenAI GPT-3.5** for answer generation
- **ChromaDB** vector database for knowledge retrieval
- **LlamaIndex** for embeddings

---

##  Repository Structure

```
full-stack-QA-application/
 backend/              # Backend API (FastAPI)
    app/             # Main application
    services/        # Business logic (PDF processing, RAG, vector store)
    models/          # Pydantic schemas
    config.py        # Configuration
    requirements.txt # Python dependencies
    .env.example     # Environment variables template
    .gitignore       # Git ignore rules
 frontend/            # Next.js frontend
    components/      # React components
    pages/           # Next.js pages
    styles/          # CSS styles
    package.json     # Node dependencies
    next.config.js   # Next.js configuration
    tsconfig.json    # TypeScript configuration
    .env.example     # Environment variables template
    .gitignore       # Git ignore rules
 data/                # PDF documents storage
 README.md            # Main documentation
 QUICKSTART.md        # Quick setup guide
 FIXES.md             # List of fixes applied
```

---

##  Features

 Upload PDF documents via UI
 Backend AI-powered Q&A using RAG (Retrieval Augmented Generation)
 Knowledge retrieval via vector search with ChromaDB
 Full stack React + FastAPI architecture
 Persistent vector storage
 TypeScript support for type safety

---

##  Getting Started

### Requirements

* **Node.js** (v18+)
* **Python** 3.9+
* **OpenAI API Key**
* **Git**

---

##  Backend Setup (FastAPI)

### 1. Navigate to backend folder
```powershell
cd backend
```

### 2. Create a virtual environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
```

### 3. Install dependencies
```powershell
pip install -r requirements.txt
```

### 4. Set environment variables
Create a `.env` file in the backend directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
VECTOR_DB_PATH=./vector_store
PDF_UPLOAD_PATH=../data
```

### 5. Run the server
```powershell
uvicorn app.main:app --reload
```

API will run at: **http://localhost:8000**

API Documentation available at: **http://localhost:8000/docs**

---

##  Frontend Setup (Next.js)

### 1. Navigate to frontend folder
```powershell
cd frontend
```

### 2. Install dependencies
```powershell
npm install
```

### 3. (Optional) Create environment file
Create a `.env.local` file:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 4. Run the app
```powershell
npm run dev
```

Frontend will open at: **http://localhost:3000**

---

##  Usage

1. Start the backend server (port 8000)
2. Start the frontend dev server (port 3000)
3. Open http://localhost:3000 in your browser
4. Upload a PDF document using the file upload interface
5. Enter questions about the document
6. View AI-generated answers based on the document content

---

##  Fixed Issues

This repository has been updated to fix the following issues:

### Backend Fixes:
-  Proper Python package structure with `__init__.py` files
-  Fixed import statements in `main.py`
-  Added persistent ChromaDB storage (instead of ephemeral)
-  Proper path handling using `pathlib`
-  Added version specifications in `requirements.txt`
-  Added Pydantic schemas for request validation
-  Added python-multipart for file uploads

### Frontend Fixes:
-  Complete `package.json` with all required dependencies
-  Proper TypeScript configuration
-  Type definitions for React components
-  Error handling in API calls
-  Loading states and user feedback
-  Input validation

### General Fixes:
-  Added `.gitignore` files for both backend and frontend
-  Added `.env.example` files for configuration templates
-  Improved documentation

---

##  Deployment

You can deploy both parts using platforms like:

-  **Vercel / Netlify**  Next.js frontend
-  **Railway / Fly.io / Render**  FastAPI backend
-  **Docker / Kubernetes**  Full production stack

---

##  API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/api/upload` | POST | Upload PDF document |
| `/api/documents` | GET | List uploaded documents |
| `/api/chat` | POST | Ask questions about documents |

---

##  Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 14, React 18, TypeScript |
| Backend | FastAPI, Uvicorn, Pydantic |
| AI/ML | OpenAI GPT-3.5, LlamaIndex |
| Vector DB | ChromaDB |
| PDF Processing | PyPDF2 |

---

##  License

MIT  2025

---

##  Contributing

We welcome contributions! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a Pull Request

---

##  Troubleshooting

### Backend won't start:
- Ensure OPENAI_API_KEY is set in `.env`
- Check that virtual environment is activated
- Verify all dependencies are installed

### Frontend connection errors:
- Ensure backend is running on port 8000
- Check CORS settings if using different origins
- Verify API URL in environment variables

### Vector store errors:
- Ensure VECTOR_DB_PATH directory has write permissions
- Check OpenAI API key is valid
- Verify ChromaDB is properly installed

---

##  Contact

For questions or support, open an issue on GitHub.

---

 Enjoy this full-stack AI Q&A project!
