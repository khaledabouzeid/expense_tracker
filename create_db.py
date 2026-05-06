import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        currency TEXT NOT NULL,
        amount_in_base REAL NOT NULL,
        date TEXT NOT NULL DEFAULT (DATE('now'))
    )
''')

conn.commit()
conn.close()
print('Database created successfully!')