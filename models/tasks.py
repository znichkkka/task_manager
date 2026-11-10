from db import get_connection


def list_tasks() -> list[dict]:
    query = """
            select tasks.*, categories.name as category_name,
                    priorities.name as priority_name, statues.name as status_name
            from tasks
            join categories on tasks.category_id = categories.id
            join priorities on tasks.priority_id = priorities.id
            join statues on tasks.status_id = statues.id
            """

    with get_connection() as connection:
        return connection.execute(query).fetchall()


def get_task(task_id: int) -> list[dict]:
    query = """
            select tasks.*, categories.name as category_name,
                    priorities.name as priority_name, statues.name as status_name
            from tasks
            join categories on tasks.category_id = categories.id
            join priorities on tasks.priority_id = priorities.id
            join statues on tasks.status_id = statues.id
            where tasks.id = %s
            """

    with get_connection() as connection:
        return connection.execute(query, (task_id, )).fetchone()