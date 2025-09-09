import sqlite3

conn = sqlite3.connect("search.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS search_terms(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    term TEXT NOT NULL UNIQUE,
    frequency INTEGER DEFAULT 0
)
""")

sample_data = {
    "laptop": 120,
    "laptop stand": 45,
    "laptop bag": 80,
    "laptop charger": 30,
    "lamp": 100,
    "lan cable": 50,
    "language learning": 70,
    "lantern": 20,
    "mobile phone": 200,
    "mobile charger": 150,
    "monitor": 90,
    "mouse": 110,
    "mug": 40
}

for term,freq in sample_data.items():
    cursor.execute("INSERT OR IGNORE INTO search_terms (term, frequency) VALUES(?,?)", (term,freq))

conn.commit()
conn.close()

print("Database setup complete")
