# Academic Writer MVP 🎓

An autonomous academic research and writing pipeline that searches for literature, downloads PDFs, synthesizes evidence, and drafts a fully-cited academic paper using Gemini 2.0 and scholarly scraping.

## 🚀 Features

- **Autonomous Research:** Generates optimized Boolean search queries based on your topic.
- **Hybrid Search Engine:** Integrates ArXiv API and Google Scholar (via `scholarly`) for comprehensive coverage.
- **Smart PDF Acquisition:** Automatically identifies and downloads open-access PDFs with an iterative quota system.
- **Evidence-Based Drafting:** Uses Gemini 2.0 Flash to parse PDFs and draft academic papers with real in-text citations.
- **Modern Dashboard:** Built with React, TypeScript, and Tailwind CSS v4, featuring a live progress tracker.
- **100% Free Stack:** Uses open-source tools and free-tier APIs.

## 🛠️ Architecture

- **Backend:** FastAPI (Python)
- **Frontend:** React (Vite) + Tailwind CSS v4
- **LLM Engine:** Google Gemini 2.0 Flash
- **Search:** ArXiv + Scholarly (Google Scholar)
- **PDF Processing:** PyPDF

## 📋 Prerequisites

- Python 3.10+
- Node.js 18+
- [Google AI Studio API Key](https://aistudio.google.com/app/apikey) (Free)

## ⚙️ Setup & Installation

### 1. Backend Setup
```bash
cd backend
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file in the `backend/` directory:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 2. Frontend Setup
```bash
cd frontend
npm install
```

## 🏃 Running the Application

### Start the Backend
```bash
cd backend
.\venv\Scripts\activate
python main.py
```
The API will be available at `http://localhost:8000`.

### Start the Frontend
```bash
cd frontend
npm run dev
```
The dashboard will be available at `http://localhost:5173`.

## 📖 Usage

1. Open the dashboard in your browser.
2. Enter a research topic and target word count.
3. Select your preferred citation style (APA, MLA, etc.).
4. Click **"Start Autonomous Research"**.
5. Monitor the live progress as the agent searches, parses, and writes your paper.

## 🛡️ License

MIT

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
