from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class AddPetFrom(FlaskForm):
  '''This will contain the from to add new pets'''

  name = StringField('Animals Name', [InputRequired()])
  species = StringField('Animals Species', validators=[InputRequired(), AnyOf(['bird', 'cat', 'dog', 'hamster'])])
  photo_url = StringField('Photo URL', validators=[Optional(), URL()])
  age = IntegerField('Animals Age', validators=[Optional(), NumberRange(min=0, max=30)])
  notes = TextAreaField('Notes about Animal')
  available = BooleanField('Is the Animal Available?')