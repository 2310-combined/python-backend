import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()  # Load environment variables from '.env' file

app = Flask(__name__)

# Configuration Classes
class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Default to a local database if no environment-specific URI is provided
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://localhost/capstone')

class DevelopmentConfig(Config):
    DEBUG = True
    # Use a specific development environment database URI or default to a local database
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI', 'postgresql://localhost/capstone_dev')

class TestConfig(Config):
    TESTING = True
    # Use a specific testing environment database URI or default to a local test database
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI', 'postgresql://localhost/capstone_test')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://localhost/capstone')
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
# Environment-specific configuration
env_config = {
    "development": DevelopmentConfig,
    "testing": TestConfig,
    "production": ProductionConfig
}

# Set the configuration from environment
config_type = os.getenv('FLASK_ENV', 'development')
app.config.from_object({
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig
}[config_type])

db = SQLAlchemy(app)