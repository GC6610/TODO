from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codechef = db.Column(db.String(200))
    codeforces = db.Column(db.String(200))
    atcoder = db.Column(db.String(200))
    hackerrank = db.Column(db.String(200))
    leetcode = db.Column(db.String(200))
    hackerearth = db.Column(db.String(200))
    github = db.Column(db.String(200))
    devfolio = db.Column(db.String(200))
    pwebsite = db.Column(db.String(200))
    linkedin = db.Column(db.String(200))
    city = db.Column(db.String(200))
    country = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
    full_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    profiles = db.relationship('Profiles')

