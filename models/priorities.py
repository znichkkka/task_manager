from db import get_connection


def list_priorities() -> list[dict]:
    with get_connection() as connection:
        return connection.execute('select id, code, name from priorities order by id').fetchall()