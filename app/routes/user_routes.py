from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.models import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    # Check for email, first_name, and last_name in the request
    if not data or not all(k in data for k in ['email', 'first_name', 'last_name']):
        return jsonify({'message': 'Missing required data'}), 400
    
    # Check if a user with this email already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'User with this email already exists'}), 409
    
    new_user = User(email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id, 'email': new_user.email, 'first_name': new_user.first_name, 'last_name': new_user.last_name}), 201

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        'id': user.id, 
        'email': user.email,
        'first_name': user.first_name, 
        'last_name': user.last_name
    }), 200

