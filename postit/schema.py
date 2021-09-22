from . import db
from flask_login import UserMixin
import datetime

"""
Se definen las tablas principales y se establece la relacion entre los usuarios y los posits que crean
"""


class Posit(db.Model):
    __tablename__ = 'posit'

    posit_id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body =  db.Column(db.Text)
    date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    category =  db.Column(db.String(20), nullable=False)
    color =  db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(280), nullable=False)
    posits = db.relationship('Posit', backref='user')
