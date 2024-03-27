import pytest
from app import create_app
from app.extensions import db as _db
from app.models.models import User, Trip
from datetime import datetime, timedelta
from config import TestConfig  # Make sure this import statement is correct (really needed this)

@pytest.fixture(scope='module')
def test_app():
    """Create and configure a new app instance for each test."""
    # Setup app with test config
    app = create_app(TestConfig)  # Adjust this according to your actual test config
    with app.app_context():
        _db.create_all()
        yield app
        _db.session.remove()
        _db.drop_all()

@pytest.fixture(scope='module')
def test_client(test_app):
    """A test client for the app."""
    return test_app.test_client()

def test_create_trip(test_client):
    # First, create a user to associate with the trip
    new_user = User(email='test@example.com', first_name='Test', last_name='User')
    _db.session.add(new_user)
    _db.session.commit()

    # Data for the new trip
    trip_data = {
        'start_location': 'Start City',
        'end_location': 'End City',
        'trip_duration': '5 hours',
        'time_of_trip': (datetime.utcnow() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
    }

    response = test_client.post(f'/users/{new_user.id}/trips', json=trip_data)
    assert response.status_code == 201
    assert 'id' in response.json

def test_get_trips(test_client):
    # Assuming a user with ID 1 exists and has trips
    response = test_client.get('/users/1/trips')
    assert response.status_code == 200
    # Validate the structure of your response data as needed

def test_delete_trip(test_client):
    # First, create a trip to be deleted
    new_trip = Trip(user_id=1, start_location='Location A', end_location='Location B', trip_duration=60, time_of_trip=(datetime.utcnow() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'))
    _db.session.add(new_trip)
    _db.session.commit()

    # Send a DELETE request to the delete_trip endpoint
    response = test_client.delete(f'/trips/{new_trip.id}')

    # Check if the trip was deleted successfully
    assert response.status_code == 200
    assert Trip.query.get(new_trip.id) is None

def test_create_user(test_client):
    # Data for the new user
    user_data = {
        'email': 'boo#booboo.com',
        'first_name': 'Ooboo',
        'last_name': 'Boo'
    }

    response = test_client.post('/users', json=user_data)
    assert response.status_code == 201
    assert 'id' in response.json

def test_show_user(test_client):
    # Assuming a user with ID 1 exists
    response = test_client.get('/users/1')
    assert response.status_code == 200
    