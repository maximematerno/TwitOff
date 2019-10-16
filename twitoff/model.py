"""SQLAlchemy models for TwitOff"""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    """Twitter users that we query and store historical tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    username = DB.Column(DB.String(15), unique=True, nullable=False)
    followers = DB.Column(DB.BigInteger, nullable=False)
    # Tweet IDs are ordinal ints, so we can fetch the most recent tweets.
    newest_tweet_id = DB.Column(DB.BigInteger, nullable=False)


class Tweet(DB.Model):
    """Stores tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    embedding = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger,
                        DB.ForeignKey('user.id'),
                        nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))   