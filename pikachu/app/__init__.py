from flask import Flask
from flask_bootstrap import Bootstrap
import random, time

app = Flask(__name__)
app.secret_key='mikorimodi'
bootstrap = Bootstrap(app)
random.seed(time.clock())
from app import routes