import os
from uuid import uuid4

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = str(uuid4().hex)
    
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_COOKIE_SECURE = False
    JWT_COOKIE_CSRF_PROJECT = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URL")

config = {
    "development": DevelopmentConfig
}
