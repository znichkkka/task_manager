from flask import Flask, render_template, request, redirect, url_for, abort

from views.tasks import tasks_bp


app = Flask(__name__, template_folder='./templates')

app.register_blueprint(tasks_bp)


@app.route('/')
def welcome_page():
    return render_template('welcome_page.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
