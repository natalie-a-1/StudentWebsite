from flask import Flask
from routes import home_blueprint, add_todo_tasks_blueprint

app = Flask(__name__)
app.register_blueprint(home_blueprint)
app.register_blueprint(add_todo_tasks_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
