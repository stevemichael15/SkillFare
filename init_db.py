import sqlite3

conn = sqlite3.connect('backend/database.db')
cursor = conn.cursor()

# Check if table exists (optional)
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
table_exists = cursor.fetchone()

if not table_exists:
    cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    print("✅ Users table created successfully.")
else:
    print("ℹ️ Users table already exists.")

conn.commit()
conn.close()
