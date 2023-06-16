from .. import db
from sqlalchemy import func
from sqlalchemy.sql import expression

class Assignment(db.Model):
    __tablename__ = 'assignments'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    deadline = db.Column(db.DateTime(timezone=True), nullable=False)
    teacher_feedback = db.Column(db.String(500))
    student_feedback = db.Column(db.String(500))
    completed = db.Column(db.Boolean, server_default=expression.false())
    student_id =  db.Column(db.Integer, db.ForeignKey('students.id'))
    student = db.relationship("Student", back_populates="assignments")
    homework_id = db.Column(db.Integer, db.ForeignKey('homework.id'))
    homework = db.relationship("Homework", back_populates="assignments")



    def __repr__(self):
        return f"Assignment(date={self.date}, deadline={self.deadline}, subject={self.homework}, student_feedback={self.student_feedback}, teacher_feedback={self.teacher_feedback},  student_id={self.student_id}, student={self.student.name}, completed={self.completed}"
