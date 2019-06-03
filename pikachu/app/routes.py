from app import app
from flask import render_template, request, redirect, url_for, session
import random
import pickle
import base64

class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.role = 'user'

USERS = {}

@app.route('/')
@app.route('/index')
def index():
    if 'id' in session:
        if session['id'] in USERS.keys():
            try:
                U = USERS[session['id']]
                u = pickle.dumps(U)
                s = base64.b64encode(u).decode('utf-8')
                return render_template('index.html', username=U.login, role=U.role, auth=s, password=U.password)
            except:
                session.pop('id', None)
        else:
            session.pop('id', None)
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'id' in session:
        return redirect('/')
    else:
        if request.method=='POST':
            if request.form['type']=='legacy':
                u = User(request.form['login'], request.form['pass'])
            else:
                s = base64.b64decode(request.form['string'])
                u = pickle.loads(s)
            id = "".join([chr(random.randint(65,91)) for i in range(32)])
            USERS[id] = u
            session['id'] = id
            print(u)
            return redirect('/')
        else:
            return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    if 'id' in session:
        if session['id'] in USERS.keys():
            del USERS[session['id']]
        session.pop('id', None)
    return redirect('/login')