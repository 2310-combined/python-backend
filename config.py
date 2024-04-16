import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()  # Load environment variables from '.env' file

app = Flask(__name__)

# Configuration Classes
class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://', 1)

class DevelopmentConfig(Config):
    DEBUG = True
    # Use a specific development environment database URI or default to a local database
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI', 'postgresql://localhost/capstone_dev')

class TestConfig(Config):
    TESTING = True
    # Use a specific testing environment database URI or default to a local test database
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI', 'postgresql://localhost/capstone_test')

class ProductionConfig(Config):
    # Use the standard Heroku environment variable or another if explicitly set
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://", 1) if os.getenv('DATABASE_URL') else 'postgresql://localhost/capstone'

# Environment-specific configuration
env_config = {
    "development": DevelopmentConfig,
    "testing": TestConfig,
    "production": ProductionConfig
}

# Set the configuration from environment
config_type = os.getenv('FLASK_ENV', 'development')
app.config.from_object(env_config[config_type])

# Initialize SQLAlchemy
db = SQLAlchemy(app)
