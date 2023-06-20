import json
from flask import request
from homeworkheroes_api.homework.routes import app


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

def test_list_homework():
    with app.test_client() as client:
        response = client.get('/homework')
        assert response.status_code == 200

def test_get_one_homework():
    with app.test_client() as client:
        response = client.get('/homework/6')
        assert response.status_code == 200

def test_update_homework():
    with app.test_client() as client:
        updated_homework = {
            "content": 'updated content',
            "subject": 'updated subject',
            "extra_resources": "updated resources",
            "homework_name": "updated homework name"
        }
        headers = {'Content-Type': 'application/json'}

        response2 = client.patch('/homework/6', data=json.dumps(updated_homework), headers=headers)

        assert response2.status_code == 200
        assert "updated content" in response2.get_json()['content']
        assert "updated subject" in response2.get_json()['subject']
        assert "updated resources" in response2.get_json()['extra_resources']
        assert "updated homework name" in response2.get_json()['homework_name']

def test_delete_homework():
    with app.test_client() as client:
        response = client.delete('/homework/17')

        response_text = response.data.decode('utf-8')

        assert 'homework deleted' in response_text
