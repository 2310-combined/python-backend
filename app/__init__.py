from flask import Flask
from .extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    return app
