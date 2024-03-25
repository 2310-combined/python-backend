import pytest
from app.extensions import db
from app.models.models import User, Trip
from datetime import datetime, timedelta

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
    trip = Trip(
        start_location="45.453, -45.666",
        end_location="34.656, -45.567",
        trip_duration="2345234",
        time_of_trip=datetime.utcnow() + timedelta(days=1),
        user=new_user
    )
    return trip

def test_new_trip(new_trip):
    assert new_trip.start_location == "45.453, -45.666"
    assert new_trip.end_location == "34.656, -45.567"
    assert new_trip.trip_duration == "2345234"
    assert isinstance(new_trip.time_of_trip, datetime)
