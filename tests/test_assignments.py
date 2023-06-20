import json
from flask import request
from homeworkheroes_api.assignments.routes import app


def test_create_assignment():
    with app.test_client() as client:
        assignment_data = {
            "deadline": "20231010",
            "student_id": 1,
            "homework_id": 8
        }
        headers = {'Content-Type': 'application/json'}

        response2 = client.post('/assignments', data=json.dumps(assignment_data), headers=headers)

        assert response2.status_code == 200

def test_list_assignments():
    with app.test_client() as client:
        response = client.get('/assignments')
        assert response.status_code == 200

def test_get_one_assignment():
    with app.test_client() as client:
        response = client.get('/assignments/3')
        assert response.status_code == 200

def test_update_assignment():
    with app.test_client() as client:
        updated_assignment = {
            "deadline": '20240101',
            "completed": True,
            "student_feedback": "student_feedback updated",
            "teacher_feedback": "teacher_feedback updated"
        }
        headers = {'Content-Type': 'application/json'}

        response2 = client.patch('/assignments/3', data=json.dumps(updated_assignment), headers=headers)

        assert response2.status_code == 200
        assert "student_feedback updated" in response2.get_json()['student_feedback']
        assert "teacher_feedback updated" in response2.get_json()['teacher_feedback']

def test_delete_assignment():
    with app.test_client() as client:
        response = client.delete('/assignments/10')

        response_text = response.data.decode('utf-8')

        assert 'assignment deleted' in response_text
