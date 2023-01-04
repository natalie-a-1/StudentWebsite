from flask import render_template, redirect, request, Blueprint
import schedule as sc

home_blueprint = Blueprint('home_blueprint', __name__, template_folder='templates')


@home_blueprint.route('/', methods=['POST', 'GET'])
def home_page():
    from app import db
    from todo import Todo
    schedule = sc.Schedule().getSchedule()
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error while adding the task'

    else:
        tasks = Todo.query.all()
    return render_template('index.html', schedule=schedule, tasks=tasks)

# @app.route('/delete/<int:id>')
# def delete(id):
#     from todo import Todo
#     task_to_delete = Todo.query.get_or_404(id)
#     try:
#         db.session.delete(task_to_delete)
#         db.session.commit()
#         return redirect('/')
#     except:
#         return 'There was an error while deleting that task'
#
#
# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     from todo import Todo
#     task = Todo.query.get_or_404(id)
#
#     if request.method == 'POST':
#         task.content = request.form['content']
#
#         try:
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue while updating that task'
#
#     else:
#         return render_template('update.html', task=task)
#
