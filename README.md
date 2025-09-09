# AutoComplete-Service

A **FastAPI + SQLite + HTML/JS** template for search autocomplete.  
This project provides a ready-to-use **autocomplete service** with frontend and backend, which can be customized with your own keywords or datasets.

---

## 🔹 Features

- Fast and lightweight **autocomplete service**.
- Supports **partial matching** and **top suggestions** based on frequency.
- Ready-to-use **frontend HTML** with dropdown suggestions.
- Can be customized with your **own search terms**.
- Designed as a **template** for integration in other projects.
- Fully **free and self-hosted** (no paid services required).

---

## 🔹 Installation (Windows)

1. **Clone the repo:**

```bash
git clone https://github.com/Prem-099/AutoComplete-Service.git
cd AutoComplete-Servcie
```

### Create virtual environment:
```bash
python -m venv venv
```

### Activate virtual environment:
```bash
venv\Scripts\activate
```

### Install dependencies:
```bash
pip install -r requirements.txt
```
### Run the FastAPI app:
```bash
uvicorn app:app --reload
```
---

### Open frontend:

Open index.html in your browser, or visit http://127.0.0.1:8000/docs for FastAPI docs.

### 🔹 Using Your Own Keywords

- By default, the project ships with sample search terms.

- You can modify the SQLite database (search.db) manually using DB Browser for SQLite.

- Optional: extend the project with /add_term or /upload_terms endpoints for bulk or dynamic uploads.

### 🔹 API Endpoints
Endpoint	Method	Description
- /autocomplete?prefix=	GET	Returns top 10 matching terms
- /search?term=	POST	Records searches (optional for analytics)

### 🔹 Frontend Usage

- Type in the search box to get real-time autocomplete suggestions.

- Click a suggestion to populate the input.

### 🔹 Customization / Template

This project is a template: users can modify the backend, database, or frontend to integrate into their own projects.

- Can be extended with:

- User-specific datasets

- Multi-user support

- CSV/JSON uploads

- Advanced ranking algorithms

---

### 🔹 Tech Stack

- Python 3.10+

- FastAPI

- SQLite (lightweight database)

- HTML, CSS, JavaScript (frontend)

- Uvicorn (ASGI server)

---

 ### 🔹 License
- This project is open-source. Free to use and modify.
