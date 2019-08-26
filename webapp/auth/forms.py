from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    name = TextField('Name', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
