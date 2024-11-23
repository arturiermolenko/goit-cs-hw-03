import os

import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

load_dotenv()


DB_NAME = os.environ["DB_NAME"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]

# SQL script to create the tables
CREATE_TABLES_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO status (name) VALUES 
    ('new'),
    ('in progress'),
    ('completed')
ON CONFLICT (name) DO NOTHING; 

CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER NOT NULL,
    user_id INTEGER,
    FOREIGN KEY (status_id) REFERENCES status(id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
"""


def create_database():
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        connection.autocommit = True
        cursor = connection.cursor()

        cursor.execute(
            sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"),
            [DB_NAME],
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(
                sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME))
            )
            print(f"Database '{DB_NAME}' created successfully.")
        else:
            print(f"Database '{DB_NAME}' already exists.")

        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error creating database: {e}")


def create_tables():
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        cursor = connection.cursor()

        cursor.execute(CREATE_TABLES_SQL)
        connection.commit()
        print("Tables created successfully.")

        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error creating tables: {e}")


if __name__ == "__main__":
    create_database()
    create_tables()
