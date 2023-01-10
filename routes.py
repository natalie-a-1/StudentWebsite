from flask import render_template, redirect, request, Blueprint, url_for
import schedule as sc
from database import get_todo_tasks, add_todo_tasks, delete_todo_tasks

home_blueprint = Blueprint('home_blueprint', __name__)


@home_blueprint.route('/', methods=['GET', 'POST'])
def home_page():
    schedule = sc.Schedule().getSchedule()
    tasks = get_todo_tasks()
    return render_template('index.html', schedule=schedule, tasks=tasks)


add_todo_tasks_blueprint = Blueprint('add_todo_tasks_blueprint', __name__)


@add_todo_tasks_blueprint.route('/add', methods=['GET', 'POST'])
def add_tasks():
    title = request.form['title']
    add_todo_tasks(title)
    return redirect(url_for('home_blueprint.home_page'))


delete_todo_tasks_blueprint = Blueprint('delete_todo_tasks_blueprint', __name__)


@delete_todo_tasks_blueprint.route('/delete', methods=['POST'])
def delete_tasks():
    id = request.form['check']
    delete_todo_tasks(id)
    return redirect(url_for('home_blueprint.home_page'))

