from .connection import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Enable foreign key constraints
    cursor.execute('PRAGMA foreign_keys = ON')

    # Create authors table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL CHECK (LENGTH(name) > 0)
        )
    ''')

    # Create magazines table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL CHECK (LENGTH(name) BETWEEN 2 AND 16),
            category TEXT NOT NULL CHECK (LENGTH(category) > 0)
        )
    ''')

    # Create articles table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL CHECK (LENGTH(title) BETWEEN 5 AND 50),
            content TEXT NOT NULL,
            author_id INTEGER,
            magazine_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors (id) ON DELETE CASCADE,
            FOREIGN KEY (magazine_id) REFERENCES magazines (id) ON DELETE CASCADE
        )
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

