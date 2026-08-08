import sqlite3


DATABASE = "storage/autodevai.db"


def get_connection():
    return sqlite3.connect(DATABASE)