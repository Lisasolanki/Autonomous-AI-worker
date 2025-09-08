from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import init_db
from orchestrator import run_pipeline
import sqlite3

app = FastAPI(title="AI Worker")

# allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# initialize database
init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/insights")
def list_insights():
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM insights ORDER BY id DESC LIMIT 20").fetchall()
    return [dict(r) for r in rows]

@app.post("/run")
def run_task():
    return run_pipeline()
