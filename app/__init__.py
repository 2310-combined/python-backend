from flask import Flask
from flask_cors import CORS
from .extensions import db, migrate
import os
import logging
from logging.handlers import RotatingFileHandler

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    
    # Load default configuration from 'config.Config' or environment-specific configuration
    config_name = os.getenv('FLASK_CONFIG', config_class)
    app.config.from_object(config_name)
    
    # Initialize CORS with default settings to allow all domains
    # Customize CORS settings as needed
    CORS(app)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Logging setup for production
    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/yourapp.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Your application startup')

    # Ensure models are known to SQLAlchemy and Flask-Migrate
    from .models import models  # Ensure this imports your User and Trip models
    
    # Import and register your Blueprints
    from .routes.user_routes import user_bp
    from .routes.trip_routes import trip_bp
    
    app.register_blueprint(user_bp)
    app.register_blueprint(trip_bp)
    
    # Additional configuration or initialization as needed

    return app
