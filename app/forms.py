from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class PetForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[(
        "cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")], validators=[InputRequired()])
    photo_url = StringField("Photo_url", validators=[Optional(), URL(
        require_tld=True, message="Must provide a valid URL")])
    age = IntegerField("Age",  validators=[Optional(), NumberRange(
        min=0, max=30, message="Ages must be between 0 - 30")])
    notes = StringField("Notes",  validators=[Optional()])
    available = BooleanField("Available", validators=[InputRequired()])


class EditPetForm(FlaskForm):
    photo_url = StringField("Photo_url", validators=[Optional(), URL(
        require_tld=True, message="Must provide a valid URL")])
    notes = StringField("Notes",  validators=[Optional()])
    available = BooleanField("Available", validators=[InputRequired()])
