from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired,Email, ValidationError, Length, EqualTo
import re

def character_check(form, field):
    excluded_chars = "*?!'^+%&/()=}][{$#@<>"
    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(f"Character {char} is not allowed")

def validate_phone(form, field):
    p = re.compile(r'^[1-9]\d{3}-\d{3}-\d{4}')
    if not p.match(field.data):
        raise ValidationError("Phone number must be in format XXXX-XXX-XXXX")

def validate_pass(form, field):
    p = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)')
    if not p.match(field.data):
        raise ValidationError("Password must contain uppercase, lowercase,"
                              " digit and special character")




class RegisterForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email("Please enter a valid email")])
    firstname = StringField(validators=[DataRequired(), character_check])
    lastname = StringField(validators=[DataRequired(), character_check])
    phone = StringField(validators=[DataRequired(), validate_phone])
    password = PasswordField(validators=[DataRequired(), Length(min=6, max=12), validate_pass])
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo("password",
                                                            message="Both password fields must be equal")])
    submit = SubmitField()
