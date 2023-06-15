from sqlalchemy import func
from flask_login import UserMixin
from .. import db

class Teacher(db.Model, UserMixin):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    school = db.Column(db.String(50), nullable=False)
    school_class = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    homeworks =  db.relationship('Homework', backref="homework_teacher")
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    role = db.Column(db.String(50), default='teacher')  # Role column for student or teacher

    def __init__(self, name, email, school, school_class, password, role=None):
        self.name = name
        self.email = email
        self.school = school
        self.school_class = school_class
        self.password = password
        self.role = role if role else 'teacher'

    def __repr__(self):
        return f"Teacher {self.name}"




# class Teacher(db.Model):
#     __tablename__ = 'teachers'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(500), nullable=False)
#     homeworks =  db.relationship('Homework', backref="homework_teacher")

#     def __repr__(self):
#         return f"Book(name={self.name}"

