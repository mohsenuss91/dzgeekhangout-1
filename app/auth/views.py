from flask import Blueprint, render_template
from app.auth.forms import LoginForm, SignUpForm

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print 'ok'

    return render_template('auth/login.html', form=form)

@auth.route('/logout')
def logout():
    pass

@auth.route('/signup')
def signup():
    pass