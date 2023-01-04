from app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(255))
    due_date = db.Column(db.DateTime())
    status = db.Column(db.String(255))

    def __rep__(self):
        return '<Task %r>' % self.id
