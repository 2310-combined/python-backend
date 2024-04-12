import pytest
from app import create_app
from app.extensions import db as _db
from app.models.models import User, Trip
from datetime import datetime, timedelta
from config import TestConfig  # Make sure this import statement is correct (really needed this)
import pdb

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
        "start_location": {
            'latitude': "40.7128",
            'longitude': "-74.006"},
        "end_location": {
            'latitude': "34.0522",
            'longitude': "-118.2437"},

        "trip_duration": '2345234',
        "time_of_trip": (datetime.utcnow() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'),
        "user_id": new_user.id
        }
    # pdb.set_trace()
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
    new_trip = Trip(user_id=1, start_location_latitude=40.7128, start_location_longitude=-74.006,
                        end_location_latitude=34.0522, end_location_longitude=-118.2437,
                        trip_duration='5 hours', time_of_trip=datetime.utcnow(), created_at=datetime.utcnow(),
                        updated_at=datetime.utcnow())
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
    
def test_user_index(test_client):
    user_data1 = {
        'email': 'boo#booboo1.com',
        'first_name': 'Ooboo1',
        'last_name': 'Boo1'
    }

    user_data2 = {
        'email': 'boo#booboo1.com',
        'first_name': 'Ooboo1',
        'last_name': 'Boo1'
    }

    test_client.post('/users', json=user_data1)
    test_client.post('/users', json=user_data2)

    response = test_client.get('/users')
    assert response.status_code == 200
    assert len(response.json) == 3 # 3 because there are 2 users and one from earlier test

def test_update_user(test_client):
    # First, create a user to be updated
    new_user = User(email='original@example.com', first_name='Original', last_name='User')
    _db.session.add(new_user)
    _db.session.commit()

    updated_data = {
        'email': 'updated@example.com',
        'first_name': 'Updated',
        'last_name': 'User'
    }

    # Send a PUT request to the update_user endpoint
    response = test_client.put(f'/users/{new_user.id}', json=updated_data)

    # Fetch the updated user from the database
    updated_user = User.query.get(new_user.id)

    # Check if the user was updated successfully
    assert response.status_code == 200
    assert updated_user.email == 'updated@example.com'
    assert updated_user.first_name == 'Updated'
    assert updated_user.last_name == 'User'
