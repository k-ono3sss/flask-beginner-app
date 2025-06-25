from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    # description = db.Column(db.Text, nullable=True)
    # deadline = db.Column(db.Date, nullable=True)
    # completed = db.Column(db.Boolean, default=False)