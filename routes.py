from flask import render_template, redirect, request, Blueprint, url_for
import schedule as sc
from database import get_todo_items, add_todo_item

home_blueprint = Blueprint('home_blueprint', __name__)


# , template_folder='templates'

@home_blueprint.route('/')
def home_page():
    schedule = sc.Schedule().getSchedule()
    tasks = get_todo_items()
    return render_template('index.html', schedule=schedule, tasks=tasks)


add_todo_item_blueprint = Blueprint('add_todo_item_blueprint', __name__)


@add_todo_item_blueprint.route('/add', methods=['POST'])
def add_item():
    title = request.form['title']
    completed = request.form['completed']
    add_todo_item(title, completed)
    return redirect(url_for('home'))
