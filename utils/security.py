import jwt
import hashlib
import os

# Function to generate a password hash
def hash_password(password):
    salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + hashed  # Store salt with hashed password

# Function to verify a password
def verify_password(stored_password, provided_password):
    salt = stored_password[:16]
    stored_hash = stored_password[16:]
    hashed_provided = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
    return stored_hash == hashed_provided

# Function to create JWT token
def create_jwt(payload, secret, algorithm='HS256'):  
    token = jwt.encode(payload, secret, algorithm=algorithm)
    return token

# Function to decode JWT token
def decode_jwt(token, secret, algorithms=['HS256']):
    try:
        payload = jwt.decode(token, secret, algorithms=algorithms)
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Invalid token