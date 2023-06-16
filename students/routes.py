
from flask import request, jsonify, make_response
from flask_login import login_required, current_user
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..app import app
from .controllers import register_student, login , logout, get_all_students,delete_student,get_student,  update_student_profile ,register_teacher,get_student_profile
from ..middleware.protected_route import protect


# @desc    Auth user & get token
# @route   POST /students
# @access  Private / protected
@app.route('/students', methods=['GET'])
def get_all_students_route():
    return get_all_students()

@app.route('/students/<id>', methods=['DELETE', 'GET'])
def student(id):
    if request.method == 'DELETE': return delete_student(id)
    if request.method == 'GET': return get_student(id)



# @desc    Register a new user
# @route   POST /register
# @access  Public
@app.route('/register',methods=['POST'])
def add_student():
    return register_student()


@app.route('/login', methods=['POST'])
def login_route():
    response, status_code = login()
    if response is not None and 'access_token' in response.json:
        access_token = response.json['access_token']
        response = make_response(response)
        response.set_cookie('access_token', access_token)
    return response, status_code

    # return login()

# @desc    Logout user / clear cookie
# @route   POST /logout
# @access  Public
@app.route('/logout', methods=['GET', 'POST'])
def logout_route():
    response = logout()
    return unset_cookie(response, 'access_token')
    # return logout()


# Error handlers
@app.errorhandler(401)
def unauthorized(error):
    return jsonify(message='Unauthorized'), 401

#@app.route('/protected')
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({'message': 'Protected route', 'user': current_user}), 200

def set_cookie(response, name, value):
    response.set_cookie(name, value=value, httponly=True)
    return response


def unset_cookie(response, name):
    response = make_response(response)  # Convert the tuple response to a Response object
    response.delete_cookie(name)
    return response


# Route for teacher registration
@app.route('/teachers/register', methods=['POST'])
def register_teacher_route():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    school = data.get('school')
    school_class = data.get('school_class')
    role=data.get('role')
    password = data.get('password')

    if not name or not email or not school or not school_class or not password:
        return jsonify(message="Missing required fields"), 400

    response = register_teacher(name, email, school, school_class, role, password)

    return response


#  @desc    Get user profile AND Update user profile
#  @route   GET /students/profile
#  @access  Private
@app.route('/student/profile/<id>', methods=['GET','PUT'])

def profile(id):
    if request.method == 'GET': return get_student_profile(id)
    if request.method == 'PUT': return update_student_profile(id)










# # Protected route accessible by students
# @app.route('/students/dashboard',methods=['GET','POST'])
# # @protect(['student'])
# @login_required
# # @jwt_required()
# def student_dashboard():
#     if current_user.role == 'student':

#         # Only accessible by students
#         return jsonify(message="Welcome to the student dashboard!")
#     else:
#         return jsonify(message="Access denied")

# # Protected route accessible by teachers
# @app.route('/teachers/dashboard',methods=['GET','POST'])
# @protect(['teacher'])
# # @login_required
# def teacher_dashboard():
#     if current_user.role == 'teacher':

#         # Only accessible by teachers
#         return jsonify(message="Welcome to the teacher dashboard!"),200
#     else:
#         return jsonify(message="Access denied"), 401
