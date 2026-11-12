from flask import render_template, request, redirect, url_for, abort, Blueprint

from models.tasks import list_tasks, get_task, create_task, update_task, delete_task
from models.categories import list_categories
from models.priorities import list_priorities
from models.statuses import list_statuses
from views.helpers import read_form, validate_task


tasks_bp = Blueprint('tasks_bp', __name__, template_folder='../templates')


@tasks_bp.route('/tasks')
def index():
    tasks = list_tasks()
    return  render_template('index.html', tasks=tasks)


@tasks_bp.route('/tasks/<int:task_id>')
def detail(task_id: int):
    task = get_task(task_id)
    return render_template('detail.html', task=task)


@tasks_bp.route('/tasks/new', methods=['GET', 'POST'])
def create():
    category_list = list_categories()
    priority_list = list_priorities()
    status_list = list_statuses()
    task = {'title': '', 'description': '', 'category_id': '', 'priority_id': '', 'status_id': ''}
    error = ''

    if request.method == 'POST':
        task = read_form()
        error = validate_task(task, category_list, priority_list, status_list)

        if not error:
            task_id = create_task(task)
            return redirect(url_for('tasks_bp.detail', task_id=task_id))

    return render_template('form.html', task=task, error=error,
                           categories=category_list, priorities=priority_list, statuses=status_list)


@tasks_bp.route('/tasks/<int:task_id>/edit', methods=["GET", "POST"])
def edit(task_id: int):
    task = get_task(task_id=task_id)
    if task is None:
        abort(404)

    task['category_id'] = str(task['category_id'])
    task['priority_id'] = str(task['priority_id'])
    task['status_id'] = str(task['status_id'])

    category_list = list_categories()
    priority_list = list_priorities()
    status_list = list_statuses()
    error = ''

    if request.method == 'POST':
        task = read_form()
        error = validate_task(task, category_list, priority_list, status_list)

        if not error:
            update_task(task_id, task)
            return redirect(url_for('tasks_bp.detail', task_id=task_id))

    return render_template('form.html', task=task, error=error,
                           categories=category_list, priorities=priority_list, statuses=status_list)


@tasks_bp.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete(task_id):
    task = get_task(task_id)
    if not task:
        abort(404)

    delete_task(task_id)
    return redirect(url_for('tasks_bp.index'))
