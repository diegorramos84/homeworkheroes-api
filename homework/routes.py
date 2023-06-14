from flask import request

from ..app import app
from .controllers import get_all_homeworks, get_one_homework, create_homework, update_homework, delete_homework

@app.route("/homework", methods=['GET', 'POST'])
def list_homework():
    if request.method == 'GET': return get_all_homeworks()
    if request.method == 'POST': return create_homework()

@app.route("/homework/<id>", methods=['GET', 'PATCH', 'DELETE'])
def get_homework(id):
    if request.method == 'GET': return get_one_homework(id)
    if request.method == 'PATCH': return update_homework(id)
    if request.method == 'DELETE': return delete_homework(id)
