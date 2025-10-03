from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "super-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/site.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "login"

    # Import blueprints
    from .weather import weather_bp

    app.register_blueprint(weather_bp)

    # Import models so db.create_all() knows them
    from . import models

    # Create database tables if not exist
    with app.app_context():
        db.create_all()

    # Basic route
    @app.route("/")
    def home():
        return "<h1>Pine Lake Website Home</h1>"

    return app

    app.register_blueprint(weather_bp)

    # Example home route
    @app.route("/")
    def home():
        return "✅ Pine Lake App is running!"

    return app
