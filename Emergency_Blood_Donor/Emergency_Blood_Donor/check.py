import sqlite3

conn = sqlite3.connect("blood.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM donors")

rows = cursor.fetchall()

print("Donors List:\n")

for row in rows:
    print(row)

conn.close()