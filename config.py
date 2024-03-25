import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://scott:password123@localhost/scott'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
                            'postgresql://scott:password123@localhost/scott'

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
                            'postgresql://scott:password123@localhost/scott_test'
    # Any other test-specific settings

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
                            'postgresql://scott:password123@localhost/scott'