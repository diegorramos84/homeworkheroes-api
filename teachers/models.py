from .. import db

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    homeworks =  db.relationship('Homework', backref="homework_teacher")

    def __repr__(self):
        return f"Book(name={self.name}"
