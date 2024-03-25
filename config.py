import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://nathan:please@localhost/capstone'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
                            'postgresql://nathan:please@localhost/capstone'

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
                            'postgresql://nathan:please@localhost/capstone_test'
    # Any other test-specific settings

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
                            'postgresql://nathan:please@localhost/capstone'