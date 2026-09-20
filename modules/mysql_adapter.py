from pymysqlpool import ConnectionPool
import pymysql.cursors

from modules.logger import logger

import config

pool = ConnectionPool(
    size=3,
    maxsize=10,
    name="pool",
    host=config.MYSQL_HOST,
    port=config.MYSQL_PORT,
    user=config.MYSQL_USER,
    password=config.MYSQL_PASSWORD,
    database=config.MYSQL_DATABASE,
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)

def sub(sender: str, enable: int):
    with pool.get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id FROM sub_users WHERE identity_hash = %s",
                (sender,)
            )
            result = cursor.fetchone()

            if not result:
                cursor.execute(
                    """
INSERT INTO sub_users
(identity_hash, subscribed)
VALUES (%s, %s)""",
                    (sender, enable,)
                )
                return

            cursor.execute(
                "UPDATE sub_users SET subscribed = %s WHERE identity_hash = %s",
                (enable, sender,)
            )

def write_message(text):
    with pool.get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
INSERT INTO messages_history
(text)
VALUES (%s)""",
                (text,)
            )

def get_subscribed():
    with pool.get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
SELECT identity_hash FROM sub_users
WHERE subscribed = 1
""")
            return cursor.fetchall()
        

def get_last_message():
    with pool.get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
SELECT * FROM messages_history
WHERE id = (SELECT MAX(id) FROM messages_history);
"""
            )
            return cursor.fetchone()
