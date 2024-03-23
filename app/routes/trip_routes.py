from flask import Blueprint, request, jsonify
# Corrected import statement for db
from app.extensions import db
from app.models.models import User, Trip
from datetime import datetime

# Define the Blueprint for trip routes
trip_bp = Blueprint('trip_bp', __name__)

@trip_bp.route('/users/<int:user_id>/trips', methods=['POST'])
def create_trip(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    # Check for required fields in the request
    required_fields = ['start_location', 'end_location', 'trip_duration', 'time_of_trip']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing required data'}), 400

    new_trip = Trip(
        user_id=user.id,
        start_location=data['start_location'],
        end_location=data['end_location'],
        trip_duration=data['trip_duration'],
        time_of_trip=datetime.strptime(data['time_of_trip'], '%Y-%m-%d %H:%M:%S')  # Adjust format as needed
    )
    db.session.add(new_trip)
    db.session.commit()
    return jsonify({'id': new_trip.id, 'start_location': new_trip.start_location, 'end_location': new_trip.end_location, 'trip_duration': new_trip.trip_duration, 'time_of_trip': new_trip.time_of_trip}), 201

@trip_bp.route('/users/<int:user_id>/trips', methods=['GET'])
def get_trips(user_id):
    trips = Trip.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': trip.id,
        'start_location': trip.start_location,
        'end_location': trip.end_location,
        'trip_duration': trip.trip_duration,
        'time_of_trip': trip.time_of_trip.strftime('%Y-%m-%d %H:%M:%S')  # Adjust format as needed
    } for trip in trips]), 200
