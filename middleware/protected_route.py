from functools import wraps
from flask import request, jsonify
import os
import jwt
from dotenv import load_dotenv

from ..students.models import Student, Teacher

load_dotenv()

def protect(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            access_token = request.cookies.get('access_token')
            print("access_token:", access_token) 
            if access_token:
                jwt_secret = os.getenv('JWT_SECRET')
                print("JWT Secret:", jwt_secret) 
                try:
                    decoded = jwt.decode(access_token, jwt_secret, algorithms=['HS256'])
                    print("decoded:", decoded)
                    student_id = decoded.get('student_id')
                    teacher_id = decoded.get('teacher_id')
                    print("student_id:", student_id)
                    
                    student = Student.query.filter_by(id=student_id).first()
                    teacher = Teacher.query.filter_by(id=teacher_id).first()

                    if not student:
                        return jsonify(error='Not authorized, student not found'), 401

                    if 'Teacher' in role and request.path.startswith('/teachers'):
                        request.teacher = teacher
                        print("Student:", request.student)
                        return func(*args, **kwargs)
                    elif 'Student' in role and request.path.startswith('/students'):
                        request.student = student
                        return func(*args, **kwargs)
                    else:
                        return jsonify(error='Not authorized, invalid role'), 403
                except jwt.exceptions.ExpiredSignatureError:
                    return jsonify(error='Not authorized, token expired'), 401
                except jwt.exceptions.InvalidTokenError:
                    return jsonify(error='Not authorized, invalid token'), 401
            else:
                return jsonify(error='Not authorized, no token'), 401

        return wrapper

    return decorator


