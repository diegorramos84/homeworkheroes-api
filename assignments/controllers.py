from flask import request, jsonify

from .. import db
from .models import Assignment

def get_all_assignments():
    assignments = Assignment.query.all()
    assignments_list = []
    for a in assignments:
        ass = {
            "id": a.id,
            "date": a.date,
            "deadline": a.deadline,
            "feedback": a.feedback,
            "completed": a.completed,
            "student": a.student.name,
            "student_id": a.student_id,
            "subject": a.homework.subject,
            "content": a.homework.content,
            "extra_resources": a.homework.extra_resources,
            "teacher": a.homework.teacher.name,
            "teacher_id": a.homework.teacher_id,
            "homework_id": a.homework_id
        }
        assignments_list.append(ass)
    return jsonify(assignments_list)


def get_one_assignment(id):
    a = Assignment.query.get(id)

    ass = {
        "id": a.id,
        "date": a.date,
        "deadline": a.deadline,
        "feedback": a.feedback,
        "completed": a.completed,
        "student": a.student.name,
        "student_id": a.student_id,
        "subject": a.homework.subject,
        "content": a.homework.content,
        "extra_resources": a.homework.extra_resources,
        "teacher": a.homework.teacher.name,
        "teacher_id": a.homework.teacher_id,
        "homework_id": a.homework_id
    }

    return jsonify(ass)

def create_assignment():
    data = request.json

    new_ass = Assignment(
        deadline = data['deadline'],
        student_id = data['student_id'],
        homework_id = data['homework_id']
    )
    db.session.add(new_ass)
    db.session.commit()

    return jsonify(id=new_ass.id, deadline=new_ass.deadline, student_id=new_ass.student_id, homework_id=new_ass.homework_id)

def update_assignment(id):
    assignment = Assignment.query.get(id)
    data = request.json

    if 'deadline' in data:
        assignment.deadline = data['deadline']
        db.session.commit()


    return jsonify(id= assignment.id, deadline=assignment.deadline)

def delete_assignment(id):
    assignment = Assignment.query.get(id)
    db.session.delete(assignment)
    db.session.commit()
    return 'assignment deleted'
