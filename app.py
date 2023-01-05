from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import home_blueprint

app = Flask(__name__)
app.register_blueprint(home_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
