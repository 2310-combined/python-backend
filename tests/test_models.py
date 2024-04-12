import pytest
from app.extensions import db
from app.models.models import User, Trip
from datetime import datetime, timedelta
import pdb


@pytest.fixture(scope='module')
def new_user():
    user = User(email="test@example.com", first_name="Test", last_name="User")
    return user

def test_new_user(new_user):
    assert new_user.email == "test@example.com"
    assert new_user.first_name == "Test"
    assert new_user.last_name == "User"

@pytest.fixture(scope='module')
def new_trip(new_user):
    trip_data = {
        "start_location": {
            'latitude': "40.7128",
            'longitude': "-74.006"},
        "end_location": {
            'latitude': "34.0522",
            'longitude': "-118.2437"},

            'trip_duration': '2345234',
            'time_of_trip': (datetime.utcnow() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'),
            'user_id': new_user.id
        }
    return trip_data

def test_new_trip(new_trip):
    # pdb.set_trace()
    assert new_trip['start_location']['latitude'] == "40.7128"
    assert new_trip['end_location']['latitude'] == "34.0522"
    assert new_trip['trip_duration'] == "2345234"


    time_of_trip_str = new_trip['time_of_trip']
    time_of_trip = datetime.strptime(time_of_trip_str, "%Y-%m-%d %H:%M:%S")
    
    assert isinstance(time_of_trip, datetime)
