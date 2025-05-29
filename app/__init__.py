# app/__init__.py
from flask import Flask
from .extensions import db, migrate
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .import_job.routes import import_bp
    app.register_blueprint(import_bp)

    return app
