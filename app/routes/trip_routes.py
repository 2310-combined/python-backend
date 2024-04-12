from flask import Blueprint, request, jsonify
# Corrected import statement for db
from app.extensions import db
from app.models.models import User, Trip
from datetime import datetime
import pdb

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


    # pdb.set_trace()
    new_trip = Trip(
        start_location_latitude = data['start_location']['latitude'],
        start_location_longitude = data['start_location']['longitude'],
        end_location_latitude = data['end_location']['latitude'],
        end_location_longitude = data['end_location']['longitude'],
        trip_duration = data['trip_duration'],
        time_of_trip = data['time_of_trip'],
        user_id = data['user_id']
    )
    
    db.session.add(new_trip)
    db.session.commit()
    return jsonify({'id': new_trip.id, 
                    'start_location': {'latitude': new_trip.start_location['latitude'], 'longitude': new_trip.start_location['longitude']},
                    'end_location': {'latitude': new_trip.end_location['latitude'], 'longitude': new_trip.end_location['longitude']}, 
                    'trip_duration': new_trip.trip_duration, 
                    'time_of_trip': new_trip.time_of_trip}), 201

@trip_bp.route('/users/<int:user_id>/trips', methods=['GET'])
def get_trips(user_id):
    trips = Trip.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': trip.id,
        'start_location': {'latitude': trip.start_location['latitude'], 'longitude': trip.start_location['longitude']},
        'end_location': {'latitude': trip.end_location['latitude'], 'longitude': trip.end_location['longitude']},
        'trip_duration': trip.trip_duration,
        'time_of_trip': trip.time_of_trip.strftime('%Y-%m-%d %H:%M:%S')  # Adjust format as needed
    } for trip in trips]), 200

@trip_bp.route('/trips/<int:trip_id>', methods=['DELETE'])
def delete_trip(trip_id):
    # Query the database to find the trip by its ID
    trip = Trip.query.get_or_404(trip_id)

    # Delete the trip from the database
    db.session.delete(trip)
    db.session.commit()

    # Return a response indicating successful deletion
    return jsonify({'message': 'Trip deleted successfully'}), 200

