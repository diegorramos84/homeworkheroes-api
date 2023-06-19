import json
from flask import request
from homeworkheroes_api.homework.routes import app, get_all_homeworks, get_one_homework, create_homework, update_homework, delete_homework

from homeworkheroes_api.students.routes import register_student, login , logout, get_all_students,delete_student,get_student,  update_student_profile ,register_teacher,get_student_profile


def test_list_homework():
    with app.test_client() as client:
        response = client.get('/homework')
        assert response.status_code == 200

def test_create_homework():
    with app.test_client() as client:
        homework_data = {
            "content": "I am content",
            "extra_resources": "www.youtube.com",
            "homework_name": "Helloooo",
            "subject": "This is a subject",
            "teacher_id": 1
        }
        headers = {'Content-Type': 'application/json'}

        response2 = client.post('/homework', data=json.dumps(homework_data), headers=headers)

        assert response2.status_code == 200
        assert "I am content" in response2.get_json()['content']
