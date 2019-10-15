from decouple import config
from dotenv import load_dotenv
from flask import Flask, render_template
from .model import DB, User

load_dotenv()

def create_app():
    """Create and configure an instance of the flask application"""
    app = Flask(__name__,template_folder='template')
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL') 
    DB.init_app(app)

    def add_user(username):
        #get twitter user data from tweepy API
        twitter_user = TWITTER.get_user(username)

        # Add user info to User table in database
        db_user = User(id=twitter_user.id, name=twitter_user.screen_name)
        DB.session.add(db_user)

    @app.route('/')
    def root():
        return render_template('home.html', users= User.query.all())

    @app.route("/about/")
    def about():
        return render_template('about.html')

    if __name__=="__main__":
        app.run(debug=True)    

    return app
