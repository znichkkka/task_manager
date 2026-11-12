from db import get_connection


def list_categories() -> list[dict]:
    with get_connection() as connection:
        return connection.execute('select id, name from categories order by id').fetchall()