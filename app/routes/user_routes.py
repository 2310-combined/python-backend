from flask import request, jsonify
from app import db
from app.models.models import User, Trip

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({'message': 'Name is required'}), 400
    new_user = User(name=data['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id, 'name': new_user.name}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name} for user in users]), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({'id': user.id, 'name': user.name}), 200