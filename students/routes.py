from flask import request

from ..app import app
from .controllers import list_all_students_controller

@app.route("/students", methods=['GET'])
def list_students():
    if request.method == 'GET': return list_all_students_controller()
