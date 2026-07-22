import sqlite3

conn = sqlite3.connect("blood.db")

cursor = conn.cursor()

cursor.execute("PRAGMA table_info(donors)")

for row in cursor.fetchall():
    print(row)

conn.close()