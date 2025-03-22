from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField


class Registerform(FlaskForm):
    username = StringField(label='USER NAME:')
    email_address = StringField(label='EMAIL-ID:')
    password = PasswordField(label='PASSWORD:')
    confirm_password = PasswordField(label='CONFIRM-PASSWORD:')
    submit = SubmitField(label='CREATE ACCOUNT ')
