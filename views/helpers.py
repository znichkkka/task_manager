from flask import request


def validate_task(task: dict, category_list: list[dict],
                  priority_list: list[dict], status_list: list[dict]) -> str:
    if not task['title']:
        return 'Введите название задачи.'
    if task['category_id'] not in [str(category['id']) for category in category_list]:
        return 'Выберите существующую категорию.'
    if task['priority_id'] not in [str(priority['id']) for priority in priority_list]:
        return 'Выберите существующий приоритет.'
    if task['status_id'] not in [str(status['id']) for status in status_list]:
        return 'Выберите существующий статус.'
    return ''


def read_form() -> dict:
    return {
            'title': request.form.get('title', '').strip(),
            'description': request.form.get('description', ''),
            'category_id': request.form.get('category_id', ''),
            'priority_id': request.form.get('priority_id', ''),
            'status_id': request.form.get('status_id', ''),
        }
