from app import db
from flask_sqlalchemy import SQLAlchemy


class



class Increment(db.Model):
    __tablename__ = 'increments'

    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(db.String)
    time_happened = db.Column(db.String)
    shares = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    avg_cost = db.Column(db.Float(Precision=(2)))
    url = db.Column(db.String)

    def __init__(self, time_created, time_happened, shares, volume, url):
        self.username =

    def __repr__(self):
        return "<Increment()>"


investors = ['Baillie Gifford', 'Temasek']
