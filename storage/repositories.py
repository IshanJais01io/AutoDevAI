from storage.db import get_connection

def initialize_repository_table():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS repositories (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        url TEXT UNIQUE,

        language TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    connection.commit()

    connection.close()


def save_repository(name, url, language):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO repositories
        (name, url, language)
        VALUES (?, ?, ?)
        """,
        (
            name,
            url,
            language
        )
    )

    connection.commit()

    connection.close()
def get_repository_id(url):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(

        """
        SELECT id
        FROM repositories
        WHERE url=?
        """,

        (url,)

    )

    row = cursor.fetchone()

    connection.close()

    if row:

        return row[0]

    return None