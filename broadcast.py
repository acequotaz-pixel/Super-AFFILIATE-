import sqlite3
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

def get_users():
    cursor.execute("SELECT user_id FROM users")
    return cursor.fetchall()
