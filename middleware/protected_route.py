
import jwt
from functools import wraps
from flask import request, jsonify
import os
from models import User  

# logic role based access control -  authentication -> based on the role of the user i.e Teacher or student 



# Custom decorator for protecting routes
def protect(allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.cookies.get('jwt')

            if token:
                try:
                    decoded = jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])
                    user_id = decoded.get('userID')

                    # Fetch user based on the user ID from the token
                    user = User.query.filter_by(id=user_id).first()

                    if not user:
                        return jsonify(error='Not authorized, user not found'), 401

                    # Check user role and allow access based on role
                    if 'teacher' in allowed_roles and request.path.startswith('/teachers'):
                        # Teacher role accessing teachers side of the app
                        request.user = user
                        return func(*args, **kwargs)
                    elif 'student' in allowed_roles and request.path.startswith('/students'):
                        # Student role accessing students side of the app
                        request.user = user
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
