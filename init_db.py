from pathlib import Path

from psycopg import Connection

from db import get_connection

PROJECT_DIR_PATH = Path(__file__).resolve().parent


def create_tables(connection: Connection) -> None:
    query = (PROJECT_DIR_PATH / 'schema.sql').read_text(encoding='utf-8')
    connection.execute(query)


def fill_tables(connection: Connection) -> None:
    query = (PROJECT_DIR_PATH / 'seed.sql').read_text(encoding='utf-8')
    connection.execute(query)


if __name__ == '__main__':
    with get_connection() as conn:
        create_tables(conn)
        fill_tables(conn)
    print('Таблицы созданы и заполнены данными')
