
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
    password = db.Column(db.String(130), nullable=False)
    # assignments = db.relationship("Assignment", backref="assignment_student")
    assignments = db.relationship("Assignment", back_populates="student", cascade="all, delete-orphan")
    avatar = db.Column(db.String(200))  # Image path or URL column
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    role = db.Column(db.String(50), default='student')  # Role column for student or teacher

    def __repr__(self):
        return f"Student(name={self.name}, superpower={self.superpower},  date_of_birth={self.date_of_birth}, level={self.level}, assignments={self.assignments}"
