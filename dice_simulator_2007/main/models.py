from flask.ext.sqlalchemy import SQLAlchemy
import datetime
from main import app

db = SQLAlchemy(app)


class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, index=True)
    password = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, index=True)
    dateofreg = db.Column(db.DateTime, default=datetime.datetime.now)
    balance = db.Column(db.String(50))

    def __init__(self, firstname, lastname, username, password, email, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email
        self.balance = balance

db.create_all()
