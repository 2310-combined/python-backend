import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))# needs to be above below logic
import pytest
from app import create_app
from app.extensions import db
from config import TestConfig  # Make sure this import statement is correct

@pytest.fixture(scope='session')
def app():
    """Instance of Main flask app configured for testing."""
    app = create_app(TestConfig)  # Pass the TestConfig class itself
    with app.app_context():
        yield app

@pytest.fixture(scope='session')
def client(app):
    """Setup Flask test client. This gets executed for each test function."""
    return app.test_client()

@pytest.fixture(scope='session')
def init_database():
    """Setup and teardown of the database."""
    db.create_all()
    yield db
    db.drop_all()
    db.session.commit()
