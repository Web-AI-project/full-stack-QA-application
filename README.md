# Full Stack Q&A Application

A full-stack **Question & Answer (Q&A)** application that lets users submit questions, retrieves answers using an AI/ML-powered backend, and displays responses in an intuitive frontend UI.

##  Built with:
- **Node.js & React** (frontend)
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
---

## 🚀 Features

✅ **Multi-File Uploads**

* Upload multiple files at once (`.txt`, `.pdf`, `.jpg`, `.jpeg`, `.png`).
* Supports **drag-and-drop** and **browse**.

✅ **Automatic File Replacement**

* Each upload replaces all previous files in the backend `/documents` folder.
* Ensures the model always reads the **latest batch** of files.

✅ **Integrated AI Chat**

* Ask GPT-4o-mini questions about your uploaded files.
* GPT automatically reads all files (text + image) each time you send a message.

✅ **Text + Image Understanding**

* Texts (PDFs, TXT) are extracted and summarized.
* Images (JPEG/PNG) are analyzed visually by GPT (via base64).

✅ **Clean React Frontend**

* Shows file previews for PDFs, text, and images.
* Real-time chat interface with markdown formatting.

✅ **Express + LangChain Backend**

* Uses `multer` for file upload handling.
* Uses `pdf-parse` for extracting text from PDFs.
* All uploaded files are stored in `/documents` folder.

---

## 🧩 Folder Structure

```
project-root/
│
├── backend/
│   ├── app.js                 # Main Node.js + Express server
│   ├── documents/             # Uploaded files (auto-cleared each upload)
│   ├── package.json
│   └── .env                   # OPENAI_API_KEY=your_key_here
│
├── frontend/
│   ├── src/
│   │   ├── App.js             # Main React UI
│   │   ├── Chat.css           # Styles
│   │   └── index.js
│   ├── package.json
│   └── public/
│
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Backend Setup

```bash
cd backend
npm install express multer pdf-parse dotenv cors @langchain/openai @langchain/core
```

Create a `.env` file inside `/backend`:

```
OPENAI_API_KEY=your_openai_api_key_here
```

Start backend:

```bash
node app.js
```

Backend runs at:

> [http://localhost:3001](http://localhost:3001)

---

### 2️⃣ Frontend Setup

```bash
cd frontend
npm install react react-dom react-markdown
npm start
```

Frontend runs at:

> [http://localhost:3000](http://localhost:3000)

---

## 💡 How It Works

### 🖼 File Upload

* When you upload or drag-drop files, they are sent to `/upload`.
* The backend deletes all previous files in `/documents` and saves the new ones.
* Supported types: `.pdf`, `.txt`, `.jpg`, `.jpeg`, `.png`.

### 📄 Chat Message

* When you send a chat message:

  1. Backend reads **all files** in `/documents`.
  2. Text is extracted from TXT/PDF.
  3. Images are converted to Base64.
  4. Everything is sent to GPT-4o-mini via LangChain.
  5. GPT’s response is returned to the frontend.

### 💬 AI Response

* GPT replies with markdown-formatted text.
* The frontend displays it in a styled chat interface.

---

## 🧠 Example Use-Case

| Type           | Example                                                        |
| -------------- | -------------------------------------------------------------- |
| 📄 PDF         | Upload a financial report → ask “Summarize the main findings.” |
| 📜 TXT         | Upload a long essay → ask “What is the conclusion?”            |
| 🖼 Image       | Upload a receipt → ask “What items were purchased?”            |
| 🗂 Multi-Files | Upload several PDFs → ask “Compare all uploaded documents.”    |

---

## 🔒 Notes

* Each upload **replaces** all previous files — ensures no outdated data remains.
* All files are stored in `/documents/` — auto-created if missing.
* No cloud storage — all local.
* You can extend this to store chat history or multiple sessions later.

---

## 🛠 Tech Stack

| Layer             | Technology                         |
| ----------------- | ---------------------------------- |
| **Frontend**      | React, ReactMarkdown               |
| **Backend**       | Node.js, Express                   |
| **AI Engine**     | OpenAI GPT-4o-mini (via LangChain) |
| **File Handling** | Multer, pdf-parse, fs/promises     |
| **Style**         | Custom CSS                         |

---
