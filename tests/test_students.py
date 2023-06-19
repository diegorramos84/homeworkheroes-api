import json
from flask import request
from homework.routes import app, get_all_homeworks, get_one_homework, create_homework, update_homework, delete_homework

from students.routes import register_student, login , logout, get_all_students,delete_student,get_student,  update_student_profile ,register_teacher,get_student_profile

def test_register_student():
    with app.test_client():
        data: