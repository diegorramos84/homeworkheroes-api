from datetime import datetime
from flask_login import UserMixin
from .. import db 
from sqlalchemy import func

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    school = db.Column(db.String(50), nullable=False)
    school_class = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    homework_id = db.Column(db.Integer)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    role = db.Column(db.String(50), default='teacher')  # Role column for student or teacher

    def __init__(self, name, email, school, school_class, superpower, date_of_birth, level, password, avatar=None, role=None):
        self.name = name
        self.email = email
        self.school = school
        self.school_class = school_class
        self.password = password
        self.role = role if role else 'student'

    def __repr__(self):
        return f"Teacher {self.name}"