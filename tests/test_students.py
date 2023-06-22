import json
import pytest
from flask import request, jsonify
# from homework.routes import app, get_all_homeworks, get_one_homework, create_homework, update_homework, delete_homework
from ..students.models import Student
# from ..students.controllers import app,  register_student, login , logout, get_all_students,delete_student,get_student,  update_student_profile ,register_teacher,get_student_profile
from ..students.routes import app, register_student, login , logout, get_all_students,delete_student,get_student,  update_student_profile ,register_teacher,get_student_profile
from .. import db
import datetime


  

def test_register_student(client):
    data = {
        "name": "test",
        "email": "testing_testing1@test.com",
        "school": "school of test",
        "school_class": "class test",
        "superpower": "Tester",
        "date_of_birth": "19800923",
        "level": "1",
        "password": "123456",
        "avatar": "/@fs/C:/Users/avnip/Desktop/homework_frontend/Homework-Heroes/src/assets/images/superhero2.png",
        "role": "student"
    }
    expected_response = {"message": "Student Created"}

    response = client.post('/register', json=data)
    assert response.status_code == 201  
    assert response.get_json() == expected_response


  # Retrieve the created student from the database
    new_student = Student.query.filter_by(email="testing_testing1@test.com").first()

    # Delete the student from the database
    db.session.delete(new_student)
    db.session.commit()

    # Check if the student is successfully deleted
    deleted_student = Student.query.filter_by(email="testing_testing@test.com").first()
    assert deleted_student is None
    
    
    db.session.delete(data)
    db.session.commit()
            
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


        
        
def delete_student(id):
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return jsonify(message='Student deleted')
    return jsonify(message='Student not found'), 404

def test_delete_existing_student(client):
    # Create a test student
    student = Student(name='John Doe')
    db.session.add(student)
    db.session.commit()

    # Make a DELETE request to delete the student
    response = client.delete(f'/students/{student.id}')

    # Validate the response status code
    assert response.status_code == 200

    # Validate the response data
    data = json.loads(response.data)
    assert data['message'] == 'Student deleted'

    # Validate that the student was deleted from the database
    assert Student.query.get(student.id) is None
    

    
def test_delete_existing_student(client):
    with app.app_context():
        # Create a test student
        student = Student(
            name='John Doe',
            email='johndoe@example.com',
            school= "Test School",
            school_class= "Class 1",
            superpower= "Tester",
            date_of_birth= "1980/09/23",
            level= 0,
            password= "123456",
            avatar= "null",
            )
        db.session.add(student)
        db.session.commit()

        # Delete the student
        response = client.delete(f'/students/{student.id}')
        assert response.status_code == 200

        # Verify that the student has been deleted from the database
        deleted_student = Student.query.get(student.id)
        assert deleted_student is None



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



import json

def test_get_all_students(client):
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




def test_get_nonexistent_student_profile(client):
    # Make a GET request to retrieve the profile of a nonexistent student
    response = client.get('/students/profile/123')

    # Validate the response status code
    assert response.status_code == 404

    # Validate the response data
    data = response.get_data(as_text=True)
    assert "Not Found" in data
    assert "The requested URL was not found on the server" in data


# def test_student_model():
#     student = Student(
#         name='John Doe',
#         email='john@example.com',
#         school='Example School',
#         school_class='Class A',
#         superpower='Invisibility',
#         date_of_birth='2000-01-01',
#         level=1,
#         password='password123',
#         avatar='avatar.png',
#         role='student'
#     )

#     assert student.name == 'John Doe'
#     assert student.email == 'john@example.com'
#     assert student.school == 'Example School'
#     assert student.school_class == 'Class A'
#     assert student.superpower == 'Invisibility'
#     assert student.date_of_birth == '2000-01-01'
#     assert student.level == 1
#     assert student.password == 'password123'
#     assert student.avatar == 'avatar.png'
#     assert student.role == 'student'


def test_get_all_students(client):
    response = client.get('/students')
    
    assert response.status_code == 200
    
    data =response.get_json()
    assert isinstance(data, list)
    
    # Assert individual student data
    for student in data:
        assert 'id' in student
        assert 'name' in student
        assert 'email' in student
        assert 'school' in student
        assert 'school_class' in student
        assert 'superpower' in student
        assert 'date_of_birth' in student
        assert 'level' in student
        assert 'role' in student
        assert 'assignments' in student
        assert 'avatar' in student
        
        # Assert assignments data
        assignments = student['assignments']
        assert isinstance(assignments, list)
        
        for assignment in assignments:
            assert 'assignment_id' in assignment
            assert 'completed' in assignment
            assert 'homework_name' in assignment
            assert 'homework_id' in assignment
            assert 'subject' in assignment
            assert 'content' in assignment
            assert 'deadline' in assignment
            assert 'student_feedback' in assignment
            assert 'teacher_feedback' in assignment
            assert 'extra-resources' in assignment
            assert 'teacher_id' in assignment
            assert 'teacher_name' in assignment
            
            
def test_get_student(client):
    # Assuming student_id is the ID of an existing student in the database
    student_id = 1
    
    response = client.get(f'/students/{student_id}')
    
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'id' in data
    assert 'name' in data
    assert 'email' in data
    assert 'school' in data
    assert 'school_class' in data
    assert 'superpower' in data
    assert 'date_of_birth' in data
    assert 'level' in data
    assert 'role' in data
    assert 'assignments' in data
    assert 'avatar' in data
    
    # Assert assignments data
    assignments = data['assignments']
    assert isinstance(assignments, list)
    
    for assignment in assignments:
        assert 'assignment_id' in assignment
        assert 'completed' in assignment
        assert 'homework_name' in assignment
        assert 'homework_id' in assignment
        assert 'subject' in assignment
        assert 'content' in assignment
        assert 'deadline' in assignment
        assert 'student_feedback' in assignment
        assert 'teacher_feedback' in assignment
        assert 'extra-resources' in assignment
        assert 'teacher_id' in assignment
        assert 'teacher_name' in assignment
        
# @pytest.fixture
# def student():
#     # Create a test student object
#     student = Student(name="John Doe", email="johndoe@example.com", password="password123")

#     return student

@pytest.fixture
def student():
    # Create a test student object
    student = Student( email="Clemens26@gmail.com", password="123456")
    return student

def test_login_student(client, student):
       
    # db.session.add(student2)
    # db.session.commit()

    # Make a POST request to login as a student
    data = {
        "email": student.email,
        "password": student.password
    }
    
    response = client.post('/login', json=data)

    # Validate the response status code
    
    assert response.status == '200 OK'
        
# def test_login_student(client, student):
   
#     # db.session.add(student)
#     # db.session.commit()

#     # Make a POST request to login as a student
#     data = {
#         "email": student.email,
#         "password": student.password
#     }
    
#     response = client.post('/login', json=data)

#     # Validate the response status code
    
#     assert response.status == '401 UNAUTHORIZED'

    # Validate the response data
    data = response.json
    assert 'access_token' in data
    assert 'id' in data
    assert 'name' in data
    assert 'email' in data
    assert 'role' in data
    assert 'school' in data
    assert 'school_class' in data
    assert 'level' in data
    assert 'avatar' in data
    
def test_get_student_profile(client):
    with app.app_context():
        # Create a test student
        test_student = Student(
            name='Test Student',
            email='teststudent1@example.com',
            school= "Test School",
            school_class= "Class 1",
            superpower= "Tester",
            date_of_birth= "19800923",
            level= 0,
            password= "123456",
            avatar= "hejs.jpg",
            role="student"
        )
        db.session.add(test_student)
        db.session.commit()

        # Send a GET request to fetch the student profile
        response = client.get(f'/students/{test_student.id}')
        assert response.status_code == 200

        # Check if the response JSON matches the expected values
        expected_response = {
            'id': test_student.id,
            'name': test_student.name,
            'email': test_student.email,
            'avatar': test_student.avatar
        }
        assert response.get_json() == expected_response

        # Delete the test student
        db.session.delete(test_student)
        db.session.commit()

    
