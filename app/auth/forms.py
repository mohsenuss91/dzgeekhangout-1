from flask_wtf import Form
from wtforms import TextField, PasswordField, validators

class LoginForm(Form):
    username = TextField('Username', validators=[validators.Required()])
    password = PasswordField('Password', validators=[validators.Required()])

class SignUpForm(LoginForm):
    
    email = TextField('Email', validators=[validators.Required()])