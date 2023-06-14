from .. import db
from sqlalchemy import func
class Homework(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    deadline = db.Column(db.DateTime(timezone=True), nullable=False)
    subject = db.Column(db.String(500), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    extra_resources = db.Column(db.String(1000))
    feedback = db.Column(db.String(1000))
    student_id =  db.Column(db.Integer, db.ForeignKey('students.id'))
    student = db.relationship("Student", back_populates="homeworks")
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    teacher = db.relationship("Teacher", back_populates="homeworks")



    def __repr__(self):
        return f"Homework(date={self.date}, deadline={self.deadline}, subject={self.subject}, content={self.content}, extra_resourcers={self.extra_resources}, feedback={self.feedback}, teacher_id={self.teacher_id}, teacher={self.teacher.name} student_id={self.student_id}, student={self.student.name}"
