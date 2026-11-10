from flask import Flask, render_template

from models.tasks import list_tasks, get_task


app = Flask(__name__, template_folder='./templates')


@app.route('/tasks')
def index():
    tasks = list_tasks()
    return  render_template('index.html', tasks=tasks)


@app.route('/tasks/<int:task_id>')
def detail(task_id: int):
    task = get_task(task_id)
    return render_template('detail.html', task=task)


if __name__ == '__main__':
    app.run(debug=True)
