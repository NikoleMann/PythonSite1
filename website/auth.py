from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/lougout')
def logout():
    return "<p>logout</p>"

@auth.route('/sigh-up')
def sign_up():
    return "<p>Sign Up</p>"