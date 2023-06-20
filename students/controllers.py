
from flask import request, jsonify, make_response
from flask_login import login_user, logout_user, current_user, login_required
from flask_jwt_extended import create_access_token, unset_jwt_cookies, unset_jwt_cookies, JWTManager,set_access_cookies
from flask_bcrypt import Bcrypt
from .. import db, login_manager,app
from sqlalchemy.orm import joinedload

from ..students.models import Student
from ..teachers.models import Teacher

bcrypt = Bcrypt()
jwt = JWTManager()

@login_manager.user_loader
def load_user(student_id):
    return Student.query.get(int(student_id))


def format_student(student):
    return {
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "password": student.password,
        "school": student.school,
        "school_class": student.school_class,
        "superpower": student.superpower,
        "date_of_birth": student.date_of_birth,
        "level": student.level,
        "assignments": student.assignments,
        "avatar": student.avatar
    }

def get_all_students():
    # students = Student.query.distinct().all()
    # students = list(set(students))
    students = Student.query.options(joinedload(Student.assignments)).all()
    print('HERE!!!!!!!!!!!!!', students)
    students_list = []
    assignment_list= []
    for student in students:
        print('student', student)
        if student.assignments:
            assignments = student.assignments
            for a in assignments:
                assignment = {
                "assignment_id": a.id,
                "completed": a.completed,
                "homework_name": a.homework.homework_name,
                "homework_id": a.homework.id,
                "subject": a.homework.subject,
                "content": a.homework.content,
                "deadline": a.deadline,
                "student_feedback": a.student_feedback,
                "teacher_feedback": a.teacher_feedback,
                "extra-resources": a.homework.extra_resources,
                "teacher_id": a.homework.teacher_id,
                "teacher_name": a.homework.teacher.name
            }
            assignment_list.append(assignment)
        student_data = {
            'id': student.id,
            'name': student.name,
            'email': student.email,
            "school": student.school,
            "school_class": student.school_class,
            "superpower": student.superpower,
            "date_of_birth": student.date_of_birth,
            "level": student.level,
            'role': student.role,
            'assignments': assignment_list,
            "avatar": student.avatar
        }
        students_list.append(student_data)

    return jsonify(students_list)


# Get student by ID
def get_student(id):
    student = Student.query.get(id)
    if student:
        assignment_list = []
        assignments = student.assignments
        for a in assignments:
            assignment = {
                "assignment_id": a.id,
                "completed": a.completed,
                "homework_name": a.homework.homework_name,
                "homework_id": a.homework.id,
                "subject": a.homework.subject,
                "content": a.homework.content,
                "deadline": a.deadline,
                "student_feedback": a.student_feedback,
                "teacher_feedback": a.teacher_feedback,
                "extra-resources": a.homework.extra_resources,
                "teacher_id": a.homework.teacher_id,
                "teacher_name": a.homework.teacher.name
            }
            assignment_list.append(assignment)

        student_data = {
            'id': student.id,
            'name': student.name,
            'email': student.email,
            "school": student.school,
            "school_class": student.school_class,
            "superpower": student.superpower,
            "date_of_birth": student.date_of_birth,
            "level": student.level,
            'role': student.role,
            'assignments': assignment_list,
            "avatar": student.avatar
        }
        return jsonify(student_data)

    return jsonify(message='Student not found'), 404


def delete_student(id):
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return jsonify(message='Student deleted')
    return jsonify(message='Student not found'), 404



def register_student():
    try:
        if request.method == 'POST':
            data = request.get_json()
            name = data.get('name')
            email = data.get('email')
            school = data.get('school')
            school_class = data.get('school_class')
            superpower = data.get('superpower')
            date_of_birth = data.get('date_of_birth')
            level = data.get('level')
            password = data.get('password')
            avatar = data.get('avatar')


        if not name or not email or not password or not school or not school_class or not superpower or not date_of_birth or not level:
            return jsonify(message="There are some missing field's, all fields are required"), 400
        email_exists = Student.query.filter_by(email=email).first()
        if email_exists:
            return jsonify(message=" Email is already in use"), 400
        elif len(password) < 6:
            return jsonify(message=" Password is too short "), 400
        elif len(email) < 4:
            return jsonify(message="Email is invalid"), 400
        else:

           # Generate the salted password hash
            hashed_password = bcrypt.generate_password_hash(
                password).decode('utf-8')

            # create new student instance
            new_student = Student(
                name=name,
                email=email,
                school=school,
                school_class=school_class,
                superpower=superpower,
                date_of_birth=date_of_birth,
                level=level,
                password=hashed_password,
                avatar=avatar  # Assign the avatar field
            )

        db.session.add(new_student)
        db.session.commit()
        login_user(new_student, remember=True)
        return jsonify(message="Student Created"), 201

    except Exception as e:
        return (str(e))


def login():
    try:
        if request.method == 'POST':
            data = request.get_json()
            email = data.get("email")
            password = data.get('password')

            if not email or not password:
                return jsonify(message="Email and password are required"), 400

            student = Student.query.filter_by(email=email).first()
            teacher = Teacher.query.filter_by(email=email).first()

            print("teacher:", teacher)

            if student and bcrypt.check_password_hash(student.password, password):
                login_user(student)
                access_token = create_access_token(identity=student.id)
                response = make_response(jsonify(
                    access_token=access_token,
                    id=student.id,
                    name=student.name,
                    email=student.email,
                    role=student.role,
                    school=student.school,
                    school_class=student.school_class,
                    level=student.level,
                    avatar=student.avatar
                    
                ))
                set_access_cookies(response, access_token)
                return response, 200

            if teacher and bcrypt.check_password_hash(teacher.password, password):
                login_user(teacher)
                access_token = create_access_token(identity=teacher.id)
                print('access_toke:', access_token)
                response = make_response(jsonify(
                    access_token=access_token,
                    id=teacher.id,
                    name=teacher.name,
                    email=teacher.email,
                    role=teacher.role,
                    school=student.school,
                    school_class=student.school_class,
                    level=student.level,
                    avatar=student.avatar
                ))
                set_access_cookies(response, access_token)
                print('response:', response)
                return response, 200

            return jsonify(message="Invalid email or password"), 401

    except Exception as e:
        return jsonify(message="An error occurred"), 500

def logout():
    logout_user()
    return make_response(jsonify(message="user logged out successfully"),)

# def logout():
#     try:
#         if current_user.is_authenticated:
#            # logout student
#             logout_user()
#             # clear token
#             response = make_response(
#                 jsonify(message="user logged out successfully"))
#             unset_jwt_cookies(response)
#             return response

#     except Exception as e:
#         return (str(e))

@login_required
def get_student_profile(id):
    # Assuming the student ID is passed in the request headers
    # student_id = request.headers.get('student_id')
    # Fetch student from the database based on the user ID
    student = Student.query.get(id)
    # print(student)

    if student:
        return jsonify({
            'id': student.id,
            'name': student.name,
            'email': student.email,
            'avatar': student.avatar
        })
    else:
        return jsonify(error='Student not found'), 404

import bcrypt
bcrypt = Bcrypt()

# def update_student_profile(id):
#     student_id = request.json.get('student.id')
#     name = request.json.get('name')
#     email = request.json.get('email')
#     password = request.json.get('password')

#     print(request.json.get('data'))
#     if not student_id:
#         return jsonify({'error': 'Missing student_id'}), 400

#     student = Student.query.filter_by(id).first()

#     if student:
#         student.name = name or student.name
#         student.email = email or student.email

#         if password:
#             student.set_password(password)

#         db.session.commit()

#         return jsonify({
#             '_id': student.id,
#             'name': student.name,
#             'email': student.email
#         })
#     else:
#         return jsonify({'error': 'Student not found'}), 404


def update_student_profile(id):
    # Assuming the student ID is passed in the request headers
    # student_id = request.headers.get('student_id')
    # Fetch student from the database based on the student ID
    student = Student.query.get(id)
    print(student)
    if student:
        student.id = request.json.get('id', student.id)
        student.name = request.json.get('name', student.name)
        student.email = request.json.get('email', student.email)
        student.avatar = request.json.get('avatar', student.avatar)
        student.school = request.json.get('school', student.school)
        
        if 'password' in request.json:
            password = request.json.get('password')
            if password:
                # Generate the salted password hash
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                student.password = hashed_password
                db.session.commit()
            
        return jsonify({
            'id': student.id,
            'name': student.name,
            'email': student.email,
            'avatar': student.avatar,
            'school': student.school,
            'password': student.password,
        })
    else:
        return jsonify(error='Student not found'), 404



# TEACHERS

# @app.route('/register', methods=['POST'])
# Register controller for creating a new teacher
def register_teacher(name, email, school, school_class, role, password):
    # Check if the email already exists in the database
    if Teacher.query.filter_by(email=email).first():
        return jsonify(message="Email already exists"), 409

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(
                password).decode('utf-8')

    # Create a new teacher instance
    teacher = Teacher(
        name=name,
        email=email,
        school=school,
        school_class=school_class,
        role=role,
        password=hashed_password
    )

    # Add the teacher to the database
    db.session.add(teacher)
    db.session.commit()

    return jsonify(message="Teacher registered successfully"), 201


