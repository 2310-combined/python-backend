
from flask import Blueprint, request, jsonify
from app import db
from app.models.models import User, Trip

# Define the Blueprint
trip_bp = Blueprint('trip_bp', __name__)

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
