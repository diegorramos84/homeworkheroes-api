from flask import request, jsonify, make_response
from flask_login import login_required
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..app import app
from .controllers import register_student, login , logout, get_all_students,delete_student,get_student, get_student_profile, update_student_profile



# @desc    Auth user & get token
# @route   POST /students
# @access  Private / protected
@app.route('/students', methods=['GET'])
def get_all_students_route():
    return get_all_students()

@app.route('/student/<int:student_id>', methods=['DELETE', 'GET'])
def student():
    if request.method == 'DELETE': return delete_student()
    if request.method == 'GET': return get_student()


# @desc    Register a new user
# @route   POST /register
# @access  Public
@app.route('/register',methods=['POST'])
def add_student():
    return register_student()




@app.route('/login', methods=['GET','POST'])
def login_route():
    response, status_code = login()
    return set_cookie(response, 'access_token', response.json.get('access_token'))
    # return login()

# @desc    Logout user / clear cookie
# @route   POST /logout
# @access  Public
@app.route('/logout', methods=['GET', 'POST'])
def logout_route():
    response = logout()
    return unset_cookie(response, 'access_token')
    # return logout()

#  @desc    Get user profile AND Update user profile
#  @route   GET /profile
#  @access  Private
@app.route('/student/profile', methods=['GET','PUT'])
@login_required
def profile():
    if request.method == 'GET': return get_student_profile()
    if request.method == 'PUT': return update_student_profile()



# Error handlers
@app.errorhandler(401)
def unauthorized(error):
    return jsonify(message='Unauthorized'), 401

# @app.route('/protected')
# @jwt_required()
# def protected():
#     current_user = get_jwt_identity()
#     return jsonify({'message': 'Protected route', 'user': current_user}), 200

def set_cookie(response, name, value):
    response.set_cookie(name, value=value, httponly=True)
    return response


def unset_cookie(response, name):
    response = make_response(response)  # Convert the tuple response to a Response object
    response.delete_cookie(name)
    return response