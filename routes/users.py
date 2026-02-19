from flask import Blueprint, request, jsonify

# Creating a Blueprint for user routes
users_bp = Blueprint('users', __name__)

# Dummy user storage (in-memory for this example)
users = {}  # Format: {user_id: user_data}

@users_bp.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    """Endpoint to get user profile by user ID."""
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404

@users_bp.route('/user', methods=['POST'])
def create_user():
    """Endpoint to create a new user profile."""
    user_data = request.json
    user_id = user_data.get('id')
    if not user_id:
        return jsonify({'message': 'User ID is required'}), 400
    if user_id in users:
        return jsonify({'message': 'User already exists'}), 400
    users[user_id] = user_data
    return jsonify({'message': 'User created successfully'}), 201

@users_bp.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    """Endpoint to update user profile by user ID."""
    if user_id not in users:
        return jsonify({'message': 'User not found'}), 404
    user_data = request.json
    users[user_id].update(user_data)
    return jsonify({'message': 'User updated successfully'}), 200

@users_bp.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Endpoint to delete user profile by user ID."""
    if user_id in users:
        del users[user_id]
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'message': 'User not found'}), 404
