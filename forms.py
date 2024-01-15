from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Optional
from wtforms import StringField, IntegerField, BooleanField

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField('photo', validators= [Optional()])
    age = IntegerField('age', validators=[InputRequired()])
    notes = StringField('notes', validators=[Optional()])
    available= BooleanField('available', validators=[Optional()])