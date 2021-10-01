from flask import Flask
from flask_jwt import JWT
from config import Config

def register_apps(app):
    import core
    import user
    import documentation
    app.register_blueprint(core.app)
    app.register_blueprint(user.app)
    app.register_blueprint(documentation.app)

def start_jwt(app):
    from user.auth import authenticate, identity
    JWT(app, authenticate, identity)

def set_config(app):
    app.config.from_object(Config())

def create_app():
    app = Flask(__name__)
    set_config(app)

    with app.app_context():
        start_jwt(app)
        register_apps(app)
        return app
