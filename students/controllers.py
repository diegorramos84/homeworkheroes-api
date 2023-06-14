from flask import request, jsonify

from .. import db
from .models import Student

def list_all_students_controller():
    students = Student.query.all()
    assignment_list = []
    for student in students:
        assignments = student.assignments
        for a in assignments:
            assignment = {
                "completed": a.completed,
                "subject": a.homework.subject,
                "content": a.homework.content,
                "deadline": a.deadline,
                "feedback": a.feedback,
                "extra-resources": a.homework.extra_resources,
                "teacher_id": a.homework.teacher_id,
                "teacher_name": a.homework.teacher.name
            }
            assignment_list.append(assignment)

        student_obj = {
            "name": student.name,
            "superpower": student.superpower,
            "age": student.age,
            "level": student.level,
            "assignments": assignment_list
        }
    return jsonify(student_obj)
