from db import get_connection


def list_statuses() -> list[dict]:
    with get_connection() as connection:
        return connection.execute('select id, code, name from statues order by id').fetchall()