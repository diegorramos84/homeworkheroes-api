from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager
from flask_jwt_extended import JWTManager

from flask_cors import CORS

from .config import config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
jwt =JWTManager()

def create_app(config_mode):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config[config_mode])
    app.config['JWT_SECRET_KEY'] = 'abc123'

    from .students import models
    from .homework import models
    from .teachers import models
    from .assignments import models


    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    jwt.init_app(app)

    return app
