from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv

load_dotenv()

from flask_cors import CORS
  # Enable CORS for specific routes

from .config import config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
jwt =JWTManager()


def create_app(config_mode):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config[config_mode])

    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    cors = CORS(app, resources={r"/student/profile/*": {"origins": "http://localhost:5173"}})  # Enable CORS for specific routes

    from .students import models
    from .homework import models
    from .teachers import models
    from .assignments import models


    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    jwt.init_app(app)

    return app
