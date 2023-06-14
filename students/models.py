from .. import db

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    superpower = db.Column(db.String(500), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    homeworks =  db.relationship('Homework', backref="homework_student")


    def __repr__(self):
        return f"Student(name={self.name}, superpower={self.superpower}, age={self.age}, level={self.level}, homeworks={self.homeworks}"
