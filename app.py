from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/tasks-list/')
def tasks():
    return render_template("task-list.html")


@app.route('/tasks-list/<int:task_id>')
def task(task_id):
    return str(task_id)


if __name__ == '__main__':
    app.run()
