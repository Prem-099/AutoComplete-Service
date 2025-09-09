import sqlite3
from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List

app = FastAPI()

templates = Jinja2Templates(directory="templates")

def get_db_connection():
    conn = sqlite3.connect("search.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/autocomplete", response_model=List[str])
def autocomplete(prefix: str = Query(..., min_length=1)):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT term FROM search_terms WHERE term LIKE ? ORDER BY frequency DESC LIMIT 10",
        ("%" + prefix.lower() + "%",)
    )
    results = [row["term"] for row in cursor.fetchall()]
    conn.close()
    return results

@app.post("/search")
def search(term: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM search_terms WHERE term = ?", (term.lower(),))
    row = cursor.fetchone()

    if row:
        cursor.execute("UPDATE search_terms SET frequency = frequency + 1 WHERE id = ?", (row["id"],))
    else:
        cursor.execute("INSERT INTO search_terms (term, frequency) VALUES (?, 1)", (term.lower(),))

    conn.commit()
    conn.close()

    return {"message": f"Search recorded for '{term}'"}
