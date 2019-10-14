from flask import Flask
from .model import DB

def create_app():
    """Create and configure an instance of the flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////db.sqlite3'
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Hello TwitOff'

    return app
