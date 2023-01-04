from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from index import home_blueprint

app = Flask(__name__)
app.register_blueprint(home_blueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
