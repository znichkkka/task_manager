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


def create_task(task: dict) -> int:
    with get_connection() as connection:
        row = connection.execute(
            """
            insert into tasks (title, description, category_id, priority_id, status_id)
            values (%s, %s, %s, %s, %s) returning id
            """,
            (task["title"], task["description"], task["category_id"],
             task["priority_id"], task["status_id"]),
        ).fetchone()
        return row["id"]


def update_task(task_id: int, task: dict) -> None:
    with get_connection() as connection:
        connection.execute(
            """
            update tasks set title = %s, description = %s, category_id = %s,
                             priority_id = %s, status_id = %s
            where id = %s
            """,
            (task["title"], task["description"], task["category_id"],
             task["priority_id"], task["status_id"], task_id),
        )


def delete_task(task_id: int) -> None:
    with get_connection() as connection:
        connection.execute("delete from tasks where id = %s", (task_id,))