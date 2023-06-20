import json
from flask import request, jsonify
# from homework.routes import app, get_all_homeworks, get_one_homework, create_homework, update_homework, delete_homework
from ..students.models import Student
# from ..students.controllers import app,  register_student, login , logout, get_all_students,delete_student,get_student,  update_student_profile ,register_teacher,get_student_profile
from ..students.routes import app, register_student, login , logout, get_all_students,delete_student,get_student,  update_student_profile ,register_teacher,get_student_profile
from .. import db
import datetime


  

def test_register_student():
    with app.test_client() as client:
        with app.app_context():
            data={
            "name": "John Smith",
            "email": "johnsmith@test.com",
            "school": "Test School",
            "school_class": "Class 1",
            "superpower": "Tester",
            "date_of_birth": "1980/09/23",
            "level": 0,
            "password": "123456",
            "avatar": "",
        }
            headers = {"Content-Type": "application/json"}

            response = client.post('/register', data=json.dumps(data), headers=headers)
            assert response.status_code == 201
            assert response.json == {"message": "Student Created"}
            
            new_student = Student.query.filter_by(email="johnsmith@test.com").first()
            assert new_student is not None
            assert new_student.name == "John Smith"
            assert new_student.email == "johnsmith@test.com"
            assert new_student.school == "Test School"
            assert new_student.school_class == "Class 1"
            assert new_student.superpower == "Tester"
            assert new_student.date_of_birth == "1980/09/23"
            assert new_student.level == 0
            assert new_student.password != "123456"  # Check if the password was hashed
            assert new_student.avatar == ""

        # # Clean up the new_student from the database (optional)
            # db.session.delete(new_student)
            # db.session.commit()
            
def test_get_all_students(client):
    with app.test_client() as client:
        with app.app_context():
            # Create test students
            student1 = Student(name='John',password ="123456", email='john@example.com', school='ABC School', school_class='Class 1', superpower='Flying', date_of_birth=datetime.date(2001, 10, 10))
            student2 = Student(name='Jane', password ="123456", email='jane@example.com', school='XYZ School', school_class='Class 2', superpower='Invisibility', date_of_birth=datetime.date(1981, 9, 9))

            # Add the test students to the database
            db.session.add(student1)
            db.session.add(student2)
            db.session.commit()

            # Make a GET request to retrieve all students
            response = client.get('/students')

            # Validate the response status code
            assert response.status_code == 200

            # Validate the response data
            data = json.loads(response.data)
            assert isinstance(data, list)
            assert len(data) == 2
            assert data[0]['name'] == 'John'
            assert data[1]['name'] == 'Jane'


        
        
# def delete_student(id):
#     student = Student.query.get(id)
#     if student:
#         db.session.delete(student)
#         db.session.commit()
#         return jsonify(message='Student deleted')
#     return jsonify(message='Student not found'), 404

# def test_delete_existing_student(client):
#     # Create a test student
#     student = Student(name='John Doe')
#     db.session.add(student)
#     db.session.commit()

#     # Make a DELETE request to delete the student
#     response = client.delete(f'/students/{student.id}')

#     # Validate the response status code
#     assert response.status_code == 200

#     # Validate the response data
#     data = json.loads(response.data)
#     assert data['message'] == 'Student deleted'

#     # Validate that the student was deleted from the database
#     assert Student.query.get(student.id) is None
    
    
# def test_delete_existing_student(client):
#     with app.app_context():
#         # Create a test student
#         student = Student(name='John Doe', email='johndoe@example.com')
#         db.session.add(student)
#         db.session.commit()

#         # Delete the student
#         response = client.delete(f'/students/{student.id}')
#         assert response.status_code == 204

#         # Verify that the student has been deleted from the database
#         deleted_student = Student.query.get(student.id)
#         assert deleted_student is None



import json

def test_get_nonexistent_student_profile(client):
    # Make a GET request to retrieve the profile of a nonexistent student
    response = client.get('/students/profile/123')

    # Validate the response status code
    assert response.status_code == 404

    # Validate the response data
    data = response.get_data(as_text=True)
    assert "Not Found" in data
    assert "The requested URL was not found on the server" in data

