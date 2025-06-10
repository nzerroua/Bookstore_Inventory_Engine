import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Establish database connection
conn = psycopg2.connect(os.getenv("DATABASE_URL"))
conn.autocommit = True
cursor = conn.cursor()

# Initialize database schema if not exists
def init_db():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            price NUMERIC(6, 2),
            quantity INTEGER
        );
    """)

init_db()
