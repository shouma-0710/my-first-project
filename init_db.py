import sqlite3

conn = sqlite3.connect('tasks.db')
cur = conn.cursor()

cur.execute(""" 
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        done INTEGER NOT NULL DEFAULT 0
    )
""")

conn.commit()
conn.close()

print("データベースを作成しました。")