from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Voters(db.Model):
    __tablenmame__ = "voters"
    ID = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, nullable=False, unique=True)
    classnum = db.Column(db.Integer, nullable=False)
    votes = db.relationship("Votes")

    def __init__(self, student_id, classnum):
        self.student_id = student_id
        self.classnum = classnum


class Votes(db.Model):
    __tablenmame__ = "votes"
    ID = db.Column(db.Integer, primary_key=True)
    voter_id = db.Column(db.Integer, db.ForeignKey("voters.ID"), nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    choice = db.Column(db.String, nullable=False)

    def __init__(self, voter_id, category_id, choice):
        self.voter_id = voter_id
        self.category_id = category_id
        self.choice = choice
