from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    image_file = db.Column(db.String(100), nullable=True)  # Stores filename
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


class Memory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    image_filename = db.Column(db.String(100))  # optional
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    # Relationship to easily access the user who posted it
    user = db.relationship("User", backref="memories")

    def __repr__(self):
        return f"Memory('{self.title}', '{self.date_posted}')"
