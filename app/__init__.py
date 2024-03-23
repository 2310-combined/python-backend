# app/__init__.py
from flask import Flask
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)

    # Ensure models are known to SQLAlchemy and Flask-Migrate
    # by importing them here
    from .models import models

    migrate.init_app(app, db)

    from .routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    return app
