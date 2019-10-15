from decouple import config
from dotenv import load_dotenv
from flask import Flask, render_template
from .model import DB, User

def create_app():
    """Create and configure an instance of the flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/maximevacher-materno/Desktop/TwitOff/db.sqlite3' 
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Hello TwitOff'

    return app
