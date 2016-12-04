from flask import Flask, g
from flask.ext.login import LoginManager

import user_model

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'randomstuff'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user():
    try:
        return user_model.User.get(user_model.User.id == userid)
    except user_model.DoesNotExist:
        return None



@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = user_model.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close the databse function after each request"""
    g.db.close()
    return response


if __name__ == '__main__':
    user_model.initialize()
    user_model.User.create_user(username = "Kaka", email = "random@gmail.com", password = "password", admin = True)
    app.run(debug = DEBUG, port = PORT, host = HOST)
