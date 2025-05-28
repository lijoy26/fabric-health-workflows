# app/__init__.py
from flask import Flask
from .config import Config
from .user.routes import user_bp
from .utils.logger import init_logger

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize logger
    init_logger()
    
    # Register blueprints
    app.register_blueprint(user_bp, url_prefix='/user')

    return app
