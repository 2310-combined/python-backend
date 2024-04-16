import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))# needs to be above below logic
import pytest
from app import create_app
from app.extensions import db
from config import TestConfig  # Make sure this import statement is correct

@pytest.fixture(scope='session')
def app():
    """
    Create and configure a new app instance for testing.
    Use the `TestConfig` to configure the app.
    """
    app = create_app(TestConfig)
    # Push an application context to bind the SQLAlchemy object to your app
    app_context = app.app_context()
    app_context.push()
    
    db.create_all()  # Create all database tables

    yield app  # This will be used by the pytest for running the tests
    
    db.session.remove()  # Remove the session
    db.drop_all()  # Drop all database tables
    app_context.pop()  # Pop the application context

@pytest.fixture(scope='session')
def client(app):
    """
    Setup Flask test client. This gets executed for each test function.
    """
    return app.test_client()

@pytest.fixture(scope='session')
def init_database():
    """Setup and teardown of the database."""
    db.create_all()
    yield db
    db.drop_all()
    db.session.commit()
