import sqlite3

DATABASE = "storage/autodevai.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS scans (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            repository TEXT,

            language TEXT,

            files INTEGER,

            score INTEGER,

            security INTEGER,

            testing INTEGER,

            documentation INTEGER,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    connection.commit()

    connection.close()