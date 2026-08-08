from storage.db import get_connection


def save_scan(data):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(

        """

        INSERT INTO scans(

            repository,

            language,

            files,

            score,

            security,

            testing,

            documentation

        )

        VALUES(?,?,?,?,?,?,?)

        """,

        (

            data["repository"],

            data["language"],

            data["files"],

            data["score"],

            data["security"],

            data["testing"],

            data["documentation"]

        )

    )

    connection.commit()

    connection.close()


def get_latest_scan():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(

        """

        SELECT

            repository,

            language,

            files,

            score,

            security,

            testing,

            documentation,

            created_at

        FROM scans

        ORDER BY id DESC

        LIMIT 1

        """

    )

    row = cursor.fetchone()

    connection.close()

    if row is None:

        return None

    return {

        "repository": row[0],

        "language": row[1],

        "files": row[2],

        "score": row[3],

        "security": row[4],

        "testing": row[5],

        "documentation": row[6],

        "created_at": row[7]

    }


def get_last_two_scans():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(

        """

        SELECT

            score,

            security,

            testing,

            documentation,

            created_at

        FROM scans

        ORDER BY id DESC

        LIMIT 2

        """

    )

    rows = cursor.fetchall()

    connection.close()

    return rows


def get_all_scans():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT

            id,
            repository,
            language,
            files,
            score,
            security,
            testing,
            documentation,
            created_at

        FROM scans

        ORDER BY created_at DESC
        """
    )

    rows = cursor.fetchall()

    connection.close()

    return [

        {
            "id": row[0],
            "repository": row[1],
            "language": row[2],
            "files": row[3],
            "score": row[4],
            "security": row[5],
            "testing": row[6],
            "documentation": row[7],
            "created_at": row[8]
        }

        for row in rows

    ]