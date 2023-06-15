from datetime import datetime, timedelta
import jwt
import os

def generate_token(user_id):
    jwt_secret = os.getenv('JWT_SECRET')
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    access_token = jwt.encode(payload, jwt_secret, algorithm='HS256')
    return access_token