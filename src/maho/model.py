import sqlite3
from maho import config


def auto_commit(func):
    connection = sqlite3.connect(config.DB)
    cursor = connection.cursor()

    def wrapped(*args):
        func(*args, cursor=cursor)

    wrapped.cursor = cursor
    connection.commit()
    return wrapped


@auto_commit
def setup(cursor=None):
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Festive (
        Date VARCHAR(255) UNIQUE NOT NULL,
        Description VARCHAR(255) NOT NULL,
        PRIMARY KEY(Date)
    )
    """
    )


@auto_commit
def add_festivity(date, festivity, cursor=None):
    cursor.execute("INSERT INTO Festive VALUES (?, ?)", (date, festivity,))
