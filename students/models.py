from datetime import datetime
from flask_login import UserMixin
from .. import db 
from sqlalchemy import func

class Student(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    school = db.Column(db.String(50), nullable=False)
    school_class = db.Column(db.String(50), nullable=False)
    superpower = db.Column(db.String(50))
    date_of_birth = db.Column(db.DateTime, nullable=False)
    level = db.Column(db.Integer)
    password = db.Column(db.String(80), nullable=False)
    homework_id = db.Column(db.Integer)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    
    def __init__(self, name, email, school, school_class, superpower, date_of_birth, level, password):
        self.name = name
        self.email = email
        self.school = school
        self.school_class = school_class
        self.superpower = superpower
        self.date_of_birth = date_of_birth
        self.level = level
        self.password = password
      
        
    def __repr__(self):
        return f"Student {self.name}"

    