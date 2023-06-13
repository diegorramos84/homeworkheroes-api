from flask import request, jsonify, make_response
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from flask_jwt_extended import create_access_token, unset_jwt_cookies, unset_jwt_cookies,JWTManager
from flask_bcrypt import Bcrypt
from .. import db
from ..students.models import Student

bcrypt = Bcrypt()
login_manager= LoginManager()
jwt =JWTManager()

@login_manager.user_loader
def load_user(student_id):
    return Student.query.get(int(student_id))

def format_student(self):
    return {
        "name" : self.name,
        "email": self.email,
        "password" :self.password,
        "school" : self.school ,
        "school_class" : self.school_class, 
        "superpower" : self.superpower ,
        "data_of_birth" :self.date_of_birth ,
        "level" : self.level,
        "homework_id" : self.homework_id 
    }

# @app.route('/student', methods=['GET'])
def get_all_students():
    students=Student.query.all()
    students_list=[]
    
    for student in students:
       students_list.append(format_student(student))
       return jsonify(students_list)

# @app.route('/register', methods=['POST'])
def register_student():
    try:
        if request.method =='POST':
            data =request.get_json()
        name = data.get('name')
        email = data.get('email')
        school =data.get('school')
        school_class = data.get('school_class')
        superpower =data.get('superpower')
        date_of_birth =data.get('date_of_birth')
        level=data.get('level')
        password = data.get('password')
        
        if not name or not email or not password or not school or not school_class or not superpower or not date_of_birth or not level:
            return jsonify(message ="There are some missing field's, all fields are required"), 400
        email_exists = Student.query.filter_by(email=email).first()
        if email_exists:
            return jsonify(message =" Email is already in use"), 400
        elif len(password) < 6:
            return jsonify(message =" Password is too short "), 400
        elif len(email) < 4:
            return jsonify(message ="Email is invalid"), 400
        else:
            
           # Generate the salted password hash
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
      
                
            # create new student instance 
            new_student = Student( 
        name =name ,
        email = email,
        school =school,
        school_class = school_class,
        superpower =superpower,
        date_of_birth =date_of_birth,
        level= level,
        password = hashed_password,
        )
    
        db.session.add(new_student)
        db.session.commit()
        login_user(new_student, remember=True)
        return jsonify(message ="Student Created"), 201
    
    except Exception as e:
        return(str(e))
    
def login():
    try:
        data = request.get_json()
        email =data.get("email")
        password = data.get('password')
        
        if not email or not password:
            return jsonify(message="Email and password are requires"), 400
        
        student =Student.query.filter_by(email=email).first()
        if not student or not bcrypt.check_password_hash(student.password, password):
            return jsonify(message="Invalid email or password"), 401
        
        login_user(student)
        
        access_token = create_access_token(identity= student.id)
        
        response = make_response(jsonify(access_token = access_token, name=student.name, email = student.email))
        response.set_cookie('access_token', access_token)
        
        return response, 200
    
    except Exception as e:
        return(str(e))
