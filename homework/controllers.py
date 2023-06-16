from flask import request, jsonify

from .. import db
from .models import Homework

def get_all_homeworks():
    homework = Homework.query.all()
    homework_list = []
    for h in homework:
        hw = {
            "id": h.id,
            "homework_name": h.homework_name,
            "subject": h.subject,
            "content": h.content,
            "extra_resources": h.extra_resources,
            "teacher": h.teacher.name,
            "teacher_id": h.teacher_id
        }
        homework_list.append(hw)
    return jsonify(homework_list)


def get_one_homework(id):
    homework = Homework.query.get(id)

    hw = {
            "homework_name": homework.homework_name,
            "subject": homework.subject,
            "content": homework.content,
            "extra_resources": homework.extra_resources,
            "teacher": homework.teacher.name,
            "teacher_id": homework.teacher_id
        }

    return jsonify(hw)

def create_homework():
    data = request.json

    new_hw = Homework(
        homework_name = data['homework_name'],
        subject = data['subject'],
        content = data['content'],
        extra_resources = data['extra_resources'] if 'extra_resources' in data else "",
        teacher_id = data['teacher_id']
    )
    db.session.add(new_hw)
    db.session.commit()

    return jsonify(id=new_hw.id, homework_name=new_hw.homework_name, subject=new_hw.subject, content=new_hw.content, extra_resources=new_hw.extra_resources, teacher_id=new_hw.teacher_id)

def update_homework(id):
    homework = Homework.query.get(id)
    data = request.json

    if 'homework_name' in data:
        homework.homework_name = data['homework_name']
        db.session.commit()
    if 'subject' in data:
        homework.subject = data['subject']
        db.session.commit()
    if 'content' in data:
        homework.content = data['content']
        db.session.commit()
    if 'extra_resources' in data:
        homework.extra_resources = data['extra_resources']
        db.session.commit()

    return jsonify(id=homework.id, homework_name=homework.homework_name, content=homework.content, subject = homework.subject, extra_resources=homework.extra_resources, teacher_id=homework.teacher_id)

def delete_homework(id):
    homework = Homework.query.get(id)
    db.session.delete(homework)
    db.session.commit()
    return 'homework deleted'
