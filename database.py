# database.py
import os
import sqlite3
from datetime import datetime, timedelta

DATABASE_PATH = os.path.join("data", "tracker.db")

def get_db_connection():
    """Establishes and returns a database connection with dict-like row access."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the database and creates the problems table if it doesn't exist."""
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS problems (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            github_url TEXT NOT NULL,
            first_discovered TEXT NOT NULL,
            last_review_date TEXT,
            next_review_date TEXT NOT NULL,
            review_count INTEGER DEFAULT 0,
            interval_days INTEGER DEFAULT 1,
            ease_factor REAL DEFAULT 2.5,
            confidence_score INTEGER DEFAULT 0
        )
    """)
    
    conn.commit()
    conn.close()

def create_problem(name, github_url, first_discovered=None, next_review_date=None):
    """Inserts a new problem into the database. Skips or returns existing if duplicate name."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    today = datetime.now().strftime("%Y-%m-%d")
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    
    if not first_discovered:
        first_discovered = today
    if not next_review_date:
        next_review_date = tomorrow
        
    try:
        cursor.execute("""
            INSERT INTO problems (
                name, github_url, first_discovered, next_review_date, 
                review_count, interval_days, ease_factor, confidence_score
            ) VALUES (?, ?, ?, ?, 0, 1, 2.5, 0)
        """, (name, github_url, first_discovered, next_review_date))
        conn.commit()
        problem_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        # If the problem name already exists, fetch the existing one to avoid duplicates
        cursor.execute("SELECT id FROM problems WHERE name = ?", (name,))
        row = cursor.fetchone()
        problem_id = row["id"] if row else None
    finally:
        conn.close()
        
    return problem_id

def get_all_problems():
    """Retrieves all problems from the database, returned as a list of dicts."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM problems")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_problem(problem_id):
    """Retrieves a single problem by its ID. Returns dict or None."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM problems WHERE id = ?", (problem_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def update_problem(problem_id, last_review_date, next_review_date, review_count, interval_days, ease_factor, confidence_score):
    """Updates the spaced repetition parameters of an existing problem."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE problems
        SET last_review_date = ?,
            next_review_date = ?,
            review_count = ?,
            interval_days = ?,
            ease_factor = ?,
            confidence_score = ?
        WHERE id = ?
    """, (last_review_date, next_review_date, review_count, interval_days, ease_factor, confidence_score, problem_id))
    conn.commit()
    conn.close()
