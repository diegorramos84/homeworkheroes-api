from flask import request
from flask_login import login_required

from ..app import app
from .controllers import register_student, login 



@app.route('/register',methods=['POST'])
def add_student():
    return register_student()

@app.route('/login', methods=['GET','POST'])
def login_route():
     return login()
