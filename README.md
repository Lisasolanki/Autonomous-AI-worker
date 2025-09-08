 🚀 Autonomous AI Worker

The Autonomous AI Worker is a simple full-stack project that:
- Collects information (news and market data)
- Processes it using AI (or fallback demo logic if no API keys are available)
- Stores results in a local SQLite database
- Displays them on a web-based dashboard

This project connects a Python FastAPI backend  with a **React + Vite frontend** to create an easy-to-run, AI-powered dashboard.

---

## ✨ Features
- **Run Task Button**: Click a button to fetch and process new data.
- **AI Processing**: Extracts topics, summaries, and insights (using OpenAI if API key is set, otherwise generates demo content).
- **Local Database (SQLite)**: Stores generated insights with topics, summaries, and recommendations.
- **Interactive Dashboard**: Displays stored insights in a clean list format.
- **Fallback Support**: Works even without external API keys, so the project is always runnable.

---

## 🛠️ Technologies Used

### Backend
- **Python 3.10+**
- **FastAPI** → REST API framework
- **SQLite** → lightweight database
- **Uvicorn** → ASGI server
- **Requests** → for fetching news/market data
- **OpenAI API** (optional) → for summaries and insights

### Frontend
- **React** → user interface
- **Vite** → fast development server
- **Fetch API** → for communicating with backend

### Other
- **Node.js & npm** → to manage frontend dependencies
- **PowerShell (Windows)** → to run commands

---

## 📂 Project Structure
autonomous-ai-worker/
│
├── backend/
│ ├── app.py # Main FastAPI app
│ ├── models.py # Database setup (SQLite)
│ ├── orchestrator.py # Runs data pipeline
│ ├── ai.py # AI logic (topics, summary, insights)
│ ├── news.py # Fetch news
│ ├── markets.py # Fetch market data
│ └── requirements.txt # Python dependencies
│
├── frontend/
│ ├── index.html # Root HTML
│ ├── .env # Backend API URL
│ └── src/
│ ├── main.jsx # React entry point
│ ├── App.jsx # Main dashboard component
│ └── services.js # Handles API calls


## ⚙️ Setup & Execution

 1. Backend
```bash or may use powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1   # (on Windows PowerShell)
pip install -r requirements.txt
python -m uvicorn app:app --reload --port 800

Backend runs at: http://localhost:8000
Docs available at: http://localhost:8000/docs

### 2. Frontend
cd frontend
npm install
npm run dev

Frontend runs at: http://localhost:5173

Example insight:

Topics: AI, Technology
Summary:
- AI is rapidly evolving
- Market reacts positively
- Future trends expected
Recommendations:
1) Explore AI investments
2) Track new technologies
3) Watch market signals
