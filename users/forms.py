from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError
import re

def character_check(form, field):
    excluded_chars = "*?!'^+%&/()=}][{$#@<>"
    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(f"Character {char} is not allowed")




class RegisterForm(FlaskForm):
    email = StringField(validators=[DataRequired, Email])
    firstname = StringField(validators=[DataRequired, character_check])
    lastname = StringField(validators=[DataRequired, character_check])
    phone = StringField(validators=[DataRequired])
    password = PasswordField(validators=[DataRequired])
    confirm_password = PasswordField(validators=[DataRequired])
    submit = SubmitField()
