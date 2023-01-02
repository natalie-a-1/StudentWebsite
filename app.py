from urllib import request
from flask import Flask, render_template, redirect
import datetime
import schedule as sc
from todo import db, Todo

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route("/")
def home():
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


if __name__ == "__main__":
    app.run(debug=True)
