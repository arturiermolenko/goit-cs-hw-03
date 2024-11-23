import psycopg2
from faker import Faker
import random
from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

fake = Faker()


# Функція для підключення до PostgreSQL
def connect_to_db():
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )


# Функція для заповнення таблиці users
def seed_users(num_users=10):
    connection = connect_to_db()
    cursor = connection.cursor()

    for _ in range(num_users):
        fullname = fake.name()
        email = fake.email()
        cursor.execute(
            "INSERT INTO users (fullname, email) VALUES (%s, %s)",
            (fullname, email),
        )

    connection.commit()
    cursor.close()
    connection.close()
    print(f"{num_users} користувачів додано в таблицю users.")


# Функція для заповнення таблиці tasks
def seed_tasks(num_tasks=10):
    connection = connect_to_db()
    cursor = connection.cursor()

    cursor.execute("SELECT id FROM users")
    user_ids = [user[0] for user in cursor.fetchall()]

    cursor.execute("SELECT id FROM status")
    status_ids = [status[0] for status in cursor.fetchall()]

    for _ in range(num_tasks):
        title = fake.sentence(nb_words=6)
        description = fake.text(max_nb_chars=200)
        status_id = random.choice(status_ids)
        user_id = random.choice(user_ids)
        cursor.execute(
            "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
            (title, description, status_id, user_id),
        )

    connection.commit()
    cursor.close()
    connection.close()
    print(f"{num_tasks} завдань додано в таблицю tasks.")


if __name__ == "__main__":
    seed_users(20)
    seed_tasks(50)
