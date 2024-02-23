import sqlite3

con = sqlite3.connect('test_database.db')
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    user_id INT UNIQUE,
    user_name TEXT
)""")
con.commit()
