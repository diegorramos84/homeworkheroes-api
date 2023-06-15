from flask import request

from ..app import app
from .controllers import get_all_assignments, get_one_assignment, create_assignment, update_assignment, delete_assignment

@app.route("/assignments", methods=['GET', 'POST'])
def list_assignment():
    if request.method == 'GET': return get_all_assignments()
    if request.method == 'POST': return create_assignment()

@app.route("/assignments/<id>", methods=['GET', 'PATCH', 'DELETE'])
def get_assignment(id):
    if request.method == 'GET': return get_one_assignment(id)
    if request.method == 'PATCH': return update_assignment(id)
    if request.method == 'DELETE': return delete_assignment(id)
