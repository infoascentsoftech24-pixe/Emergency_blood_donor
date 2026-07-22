import sqlite3

conn = sqlite3.connect("blood.db")

cursor = conn.cursor()

cursor.execute("PRAGMA table_info(donors)")

columns = cursor.fetchall()

for col in columns:
    print(col)

conn.close()