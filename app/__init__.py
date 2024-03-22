from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes.user_routes import user_bp  # Import the user_bp Blueprint

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)

    app.register_blueprint(user_bp)  # Register the Blueprint

    with app.app_context():
        db.create_all()

    return app
