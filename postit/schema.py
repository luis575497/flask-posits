from . import db


class Posit(db.Model):
    __tablename__ = 'posit'

    posit_id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body =  db.Column(db.Text)
    date = db.Column(db.DateTime())
    category =  db.Column(db.String(20), nullable=False)
    color =  db.Column(db.String(20), nullable=False)
