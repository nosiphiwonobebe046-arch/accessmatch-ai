from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

auth = Blueprint('auth', __name__)  

# Assuming a simple in-memory user storage for demonstration purposes
users = {}  

@auth.route('/signup', methods=['POST'])
def signup():  
    data = request.get_json()  
    if 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Username and password required'}), 400  
    if data['username'] in users:
        return jsonify({'message': 'User already exists'}), 409  
    hashed_password = generate_password_hash(data['password'], method='sha256')
    users[data['username']] = hashed_password  
    return jsonify({'message': 'User created successfully'}), 201  

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Username and password required'}), 400
    user = users.get(data['username'])
    if not user or not check_password_hash(user, data['password']):
        return jsonify({'message': 'Invalid username or password'}), 401
    token = jwt.encode({'username': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'secret_key')
    return jsonify({'token': token})

@auth.route('/token', methods=['GET'])
def token():
    return jsonify({'message': 'Token endpoint'}), 200
