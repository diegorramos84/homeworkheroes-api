from flask import request
from ..app import app
from .controllers import register_student



@app.route('/register',methods=['POST'])
def add_student():
     return register_student()