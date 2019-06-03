# -*- coding: utf-8 -*- 
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.security import check_password_hash
from app import app
from app.forms import LoginForm, FeedbackForm
from app.models import User, users, get_user_by_name

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = FeedbackForm()
    if form.validate_on_submit():
        flash('Your feedback is very important to us, thank you!')
    return render_template('contact.html', title='Contact', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user_by_name(form.username.data)
        if user == None or not check_password_hash(user.pwhash, form.password.data):
            flash('Invalid credentials')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/user/<username>')
@login_required
def user(username):
    user = get_user_by_name(username)
    if user == None:
        flash('Something goes wrong')
        return redirect(url_for('index'))
    return render_template('user.html', user=user)