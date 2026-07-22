import mysql.connector
from config import *


def connect():
    return mysql.connector.connect(
        host=DATABASE_HOST,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        database=DATABASE_NAME
    )


def create_tables():

    db = connect()
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(100),
        password VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS keys_table(
        id INT AUTO_INCREMENT PRIMARY KEY,
        license_key VARCHAR(100),
        expiry_date DATE,
        status VARCHAR(20)
    )
    """)

    db.commit()
    db.close()
def save_key(key, expiry):

    db = connect()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO keys_table (license_key, expiry_date, status) VALUES (%s,%s,%s)",
        (key, expiry, "ACTIVE")
    )

    db.commit()
    db.close()
