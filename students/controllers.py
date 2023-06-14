from flask import request, jsonify

from .. import db
from .models import Student

def list_all_students_controller():
    students = Student.query.all()
    homework_list = []
    for student in students:
        homeworks = student.homeworks
        for h in homeworks:
            homework = {
                "subject": h.subject,
                "content": h.content,
                "deadline": h.deadline,
                "feedback": h.feedback,
                "extra-resources": h.extra_resources,
                "teacher_id": h.teacher_id,
                "teacher_name": h.teacher.name
            }
            homework_list.append(homework)

        student_obj = {
            "name": student.name,
            "superpower": student.superpower,
            "age": student.age,
            "level": student.level,
            "homeworks": homework_list
        }
    return jsonify(student_obj)
