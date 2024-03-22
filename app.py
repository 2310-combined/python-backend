from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nathan:please@localhost/capstone'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    # Assuming you want to link Users and Trips
    user = db.relationship('User', backref=db.backref('trips', lazy=True))

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

@app.route('/users/<int:user_id>/trips', methods=['POST'])
def create_trip(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    if not data or not data.get('destination'):
        return jsonify({'message': 'Destination is required'}), 400
    new_trip = Trip(user_id=user.id, destination=data['destination'])
    db.session.add(new_trip)
    db.session.commit()
    return jsonify({'id': new_trip.id, 'destination': new_trip.destination}), 201

@app.route('/users/<int:user_id>/trips', methods=['GET'])
def get_trips(user_id):
    trips = Trip.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': trip.id, 'destination': trip.destination} for trip in trips]), 200
