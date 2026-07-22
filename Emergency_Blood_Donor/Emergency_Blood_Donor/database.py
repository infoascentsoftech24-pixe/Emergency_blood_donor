import sqlite3

conn = sqlite3.connect("blood.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS donors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    blood_group TEXT,
    city TEXT,
    phone TEXT,
    availability TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")