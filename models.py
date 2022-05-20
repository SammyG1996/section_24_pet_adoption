'''Models for Adoption Application'''

from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# This is a method that you will be able to call in the app.py file. It will allow you to initiate the connction to the database.
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
  '''This will instantiate a new Pet in the database'''
  __tablename__ = 'pet'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)

  name = db.Column(db.String(), nullable=False)

  species = db.Column(db.String(), nullable=False)

  photo_url = db.Column(db.String())

  age = db.Column(db.Integer)

  notes = db.Column(db.String())

  available = db.Column(db.Boolean, default=True )