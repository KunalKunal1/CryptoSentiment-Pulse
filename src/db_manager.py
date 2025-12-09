import sqlite3
import pandas as pd
from datetime import datetime
import os

DB_FOLDER = "data"
DB_PATH = os.path.join(DB_FOLDER, "app_database.db")

def init_db():
    """Initialize the SQLite database and create tables if not exists."""
    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)
        
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS search_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            coin_id TEXT,
            searched_at TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def log_search(coin_id):
    """Log a user search into the database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO search_history (coin_id, searched_at) VALUES (?, ?)", 
              (coin_id, datetime.now()))
    conn.commit()
    conn.close()

def get_top_searches():
    """Retrieve top 5 searched coins."""
    # Check if DB exists first to avoid errors on first run
    if not os.path.exists(DB_PATH):
        return pd.DataFrame()

    conn = sqlite3.connect(DB_PATH)
    query = """
        SELECT coin_id, COUNT(*) as count 
        FROM search_history 
        GROUP BY coin_id 
        ORDER BY count DESC 
        LIMIT 5
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df