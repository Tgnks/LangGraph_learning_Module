
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

db_path = os.path.abspath("db.sqlite3")
print("Database location:", db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

print("Tables found:", tables)

conn.close()
