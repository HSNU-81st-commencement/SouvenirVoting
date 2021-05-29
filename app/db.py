from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Voters(db.Model):
    __tablenmame__ = "voters"
    ID = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, nullable=False, unique=True)
    classnum = db.Column(db.Integer, nullable=False)


class Votes(db.Model):
    __tablenmame__ = "votes"
    ID = db.Column(db.Integer, primary_key=True)
    voter_id = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    choice = db.Column(db.String, nullable=False)
