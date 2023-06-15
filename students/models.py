
from datetime import datetime
from flask_login import UserMixin
from .. import db 
from sqlalchemy import func

class Student(db.Model, UserMixin):
    __tablename__="students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    school = db.Column(db.String(50), nullable=False)
    school_class = db.Column(db.String(50), nullable=False)
    superpower = db.Column(db.String(50))
    date_of_birth = db.Column(db.DateTime, nullable=False)
    level = db.Column(db.Integer)
    password = db.Column(db.String(80), nullable=False)
    assignments = db.relationship("Assignment", backref="assignment_student")
    avatar = db.Column(db.String(200))  # Image path or URL column
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    role = db.Column(db.String(50), default='student')  # Role column for student or teacher

    def __init__(self, name, email, school, school_class, superpower, date_of_birth, level, password,assignments , avatar=None, role=None):
        self.name = name
        self.email = email
        self.school = school
        self.school_class = school_class
        self.superpower = superpower
        self.date_of_birth = date_of_birth
        self.level = level
        self.password = password
        self.assignments = assignments 
        self.avatar = avatar
        self.role = role if role else 'student'

     def __repr__(self):
        return f"Student(name={self.name}, superpower={self.superpower}, age={self.age}, level={self.level}, homeworks={self.assigments}"


# class Teacher(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     school = db.Column(db.String(50), nullable=False)
#     school_class = db.Column(db.String(50), nullable=False)
#     password = db.Column(db.String(80), nullable=False)
#     homework_id = db.Column(db.Integer)
#     date_created = db.Column(db.DateTime(timezone=True), default=func.now())
#     role = db.Column(db.String(50), default='teacher')  # Role column for student or teacher

#     def __init__(self, name, email, school, school_class, password, role=None):
#         self.name = name
#         self.email = email
#         self.school = school
#         self.school_class = school_class
#         self.password = password
#         self.role = role if role else 'teacher'

#     def __repr__(self):
#         return f"Teacher {self.name}"




   

