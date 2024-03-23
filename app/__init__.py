from flask import Flask
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app, db)

    # Ensure models are known to SQLAlchemy and Flask-Migrate
    from .models import models  # Ensure this imports your User and Trip models
    
    # Import and register your Blueprints
    from .routes.user_routes import user_bp
    from .routes.trip_routes import trip_bp  # Make sure this matches the name in your trip routes file
    
    app.register_blueprint(user_bp)
    app.register_blueprint(trip_bp)  # Register the trip_bp blueprint
    
    return app
