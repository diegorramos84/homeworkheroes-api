from flask import request, jsonify, make_response
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from flask_jwt_extended import create_access_token, unset_jwt_cookies, unset_jwt_cookies, JWTManager
from flask_bcrypt import Bcrypt
from .. import db
from ..students.models import Student

bcrypt = Bcrypt()
login_manager = LoginManager()
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
        "homework_id": student.homework_id,
        "avatar": student.avatar  # Include avatar field in the response
    }

# @app.route('/student', methods=['GET'])


def get_all_students():
    if request.method == 'GET':
        students = Student.query.all()
        students_list = []

        for student in students:
            students_list.append(format_student(student))

        return jsonify(students_list)

# Get student by ID


def get_student(student_id):
    student = Student.query.get(student_id)
    if student:
        return jsonify(format_student(student))
    return jsonify(message='Student not found'), 404


def delete_student(student_id):
    student = Student.query.get(student_id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return jsonify(message='Student deleted')
    return jsonify(message='Student not found'), 404


# @app.route('/register', methods=['POST'])
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
            # Get the avatar field from the request
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
        data = request.get_json()
        email = data.get("email")
        password = data.get('password')

        if not email or not password:
            return jsonify(message="Email and password are requires"), 400

        student = Student.query.filter_by(email=email).first()
        if not student or not bcrypt.check_password_hash(student.password, password):
            return jsonify(message="Invalid email or password"), 401

        login_user(student)

        access_token = create_access_token(identity=student.id)

        response = make_response(
            jsonify(access_token=access_token, name=student.name, email=student.email))
        response.set_cookie('access_token', access_token)

        return response, 200

    except Exception as e:
        return (str(e))


def logout():
    try:
        if current_user.is_authenticated:
           # logout student
            logout_user()
            # clear token
            response = make_response(
                jsonify(message="user logged out successfully"))
            unset_jwt_cookies(response)
            return response

    except Exception as e:
        return (str(e))


@login_required
def get_student_profile():
    # Assuming the student ID is passed in the request headers
    student_id = request.headers.get('student_id')
    # Fetch student from the database based on the user ID
    student = Student.query.filter_by(id=student_id).first()
    print(student)

    if student:
        return jsonify({
            '_id': student.id,
            'name': student.name,
            'email': student.email,
            'avatar': student.avatar
        })
    else:
        return jsonify(error='Student not found'), 404


def update_student_profile():
    # Assuming the student ID is passed in the request headers
    student_id = request.headers.get('student_id')
    # Fetch student from the database based on the student ID
    student = Student.query.filter_by(id=student_id).first()

    if student:
        student.name = request.json.get('name', student.name)
        student.email = request.json.get('email', student.email)
        student.avatar = request.json.get(
            'avatar', student.avatar)  # Assign the avatar field

        password = request.json.get('password')
        if password:
            student.password = password

        db.session.commit()

        return jsonify({
            '_id': student.id,
            'name': student.name,
            'email': student.email,
            'avatar': student.avatar  # Include avatar field in the response
        })
    else:
        return jsonify(error='Student not found'), 404
