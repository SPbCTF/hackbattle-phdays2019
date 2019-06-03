from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SPBCTF384129c4ae89678ec10ca19eb19617ece988f1a5179f9d46a1SPBCTF'

login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'Please sign in to view this page'

bootstrap = Bootstrap(app)

from app import routes, models, errors