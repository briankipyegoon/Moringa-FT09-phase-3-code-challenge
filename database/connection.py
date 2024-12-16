# connection.py
import sqlite3

DATABASE_NAME = './database/magazine.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)  # Replace with your actual database connection logic
    conn.row_factory = sqlite3.Row  # Ensures you can access rows as dictionaries
    return conn
