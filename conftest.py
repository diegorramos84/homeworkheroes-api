import pytest
import os
from dotenv import load_dotenv
from . import db, create_app
from .app import app

load_dotenv()

# @pytest.fixture()
# def app():
#     app = create_app(os.getenv("CONFIG_MODE"))

#     @app.route('/')
#     def hello():
#         return "<h2>Hello World!</h2>"

#     with app.app_context():
#         db.create_all()

#     yield app

#     # with app.app_context():
#     #     db.drop_all()

# @pytest.fixture
# def client(app):
#     return app.test_client()


@pytest.fixture
def client():
    app.config['TESTING'] =True
    with app.test_client()as client:
        yield client
   