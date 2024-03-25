# tests/test_routes.py
import pytest
from flask import url_for
from app import create_app

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    
    # Configure your app for testing
    flask_app.config['TESTING'] = True
    
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!

def test_home_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' route is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    # Add more assertions as needed

# Add more tests for other routes as needed
