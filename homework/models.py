from .. import db
from sqlalchemy import func

class Homework(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    homework_name = db.Column(db.String(500))
    subject = db.Column(db.String(500), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    extra_resources = db.Column(db.String(500))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    teacher = db.relationship("Teacher", back_populates="homeworks")
    assignments =  db.relationship('Assignment', backref="assignments")



    def __repr__(self):
        return f"Homework(date={self.date}, homework_name={self.homework_name}subject={self.subject}, content={self.content}, extra_resourcers={self.extra_resources}, teacher_id={self.teacher_id}, teacher={self.teacher.name}"
