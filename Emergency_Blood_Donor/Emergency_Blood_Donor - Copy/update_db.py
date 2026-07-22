import sqlite3

conn = sqlite3.connect("blood.db")

cursor = conn.cursor()

# Add new columns
try:
    cursor.execute("ALTER TABLE donors ADD COLUMN address TEXT")
    print("Address column added")
except:
    print("Address already exists")


try:
    cursor.execute("ALTER TABLE donors ADD COLUMN gender TEXT")
    print("Gender column added")
except:
    print("Gender already exists")


conn.commit()

conn.close()

print("Database updated successfully")