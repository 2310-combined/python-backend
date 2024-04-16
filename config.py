import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration Classes
class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://localhost/capstone')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI', 'postgresql://localhost/capstone_dev')

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI', 'postgresql://localhost/capstone_test')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI')

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
