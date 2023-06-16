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
            "student_feedback": a.student_feedback,
            "teacher_feedback": a.teacher_feedback,
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

    return jsonify(id=new_ass.id, deadline=new_ass.deadline, student_id=new_ass.student_id, homework_id=new_ass.homework_id, completed=new_ass.completed)

def update_assignment(id):
    assignment = Assignment.query.get(id)
    data = request.json

    if 'deadline' in data:
        assignment.deadline = data['deadline']
        db.session.commit()

    if 'completed' in data:
        assignment.completed = data['completed']
        db.session.commit()

    if 'student_feedback' in data:
        assignment.student_feedback = data['student_feedback']
        db.session.commit()

    if 'teacher_feedback' in data:
        assignment.teacher_feedback= data['teacher_feedback']
        db.session.commit()

    return jsonify(id= assignment.id, teacher_feedback=assignment.teacher_feedback, student_feedback=assignment.student_feedback, deadline=assignment.deadline, completed= assignment.completed)


def delete_assignment(id):
    assignment = Assignment.query.get(id)
    db.session.delete(assignment)
    db.session.commit()
    return 'assignment deleted'
