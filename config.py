import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Default to using a PostgreSQL database named 'capstone' on localhost
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://capstone:password123@localhost:5432/capstone')
    # postgresql://localhost/capstone

class DevelopmentConfig(Config):
    DEBUG = True
    # Look for DEV_DATABASE_URI environment variable; otherwise, use the default URI
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI', 'postgresql://localhost/capstone_dev')

class TestConfig(Config):
    TESTING = True
    # Look for TEST_DATABASE_URI environment variable; otherwise, use a separate test database
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI', 'postgresql://localhost/capstone_test')

class ProductionConfig(Config):
    # In production, DATABASE_URI must be set; there is no default.
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
