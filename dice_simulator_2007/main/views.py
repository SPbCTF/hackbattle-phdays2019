from flask import Flask, request, session, redirect, url_for, render_template, flash, jsonify
from . models import User, db
from . forms import  SignUpForm, SignInForm, AboutUserForm
from main import app
import sys
import random


@app.route('/')
def index():
    try:
        if session['user_available']:
            return render_template('index.html')
        else:
            flash('You are not a Authenticated User')
    except:
        pass

    return redirect(url_for('signin'))

@app.route('/dice', methods=['GET', 'POST'])
def dice():
    image={"bot":"/static/images/dice-cup.png", "you":"/static/images/dice-cup.png"}
    winner={"winner":"draw"}
    balance = User.query.filter_by(username=session['current_user']).first()
    if session['user_available']:
        if request.method == 'POST':
            you = random.randint(1, 6)
            bot = random.randint(3, 6)
            if you > bot:
                winner["winner"]="Winner, Winner, Chicken Dinner"
                balance.balance = str(int(balance.balance)+10)
            elif you < bot:
                winner["winner"]="Looser"
                balance.balance = str(int(balance.balance)-10)
            else:
                winner["winner"]="Draw"
            image={"bot":"/static/images/"+str(bot)+".png", "you":"/static/images/"+str(you)+".png"}
            db.session.commit()
        return render_template('dice.html', image=image, winner=winner)

    flash('User is not Authenticated')
    return redirect(url_for('signin'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signupform = SignUpForm(request.form)
    if request.method == 'POST':
        reg = User(signupform.firstname.data, signupform.lastname.data,\
        signupform.username.data, signupform.password.data,\
        signupform.email.data, "100")
        db.session.add(reg)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('signup.html', signupform=signupform)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    user = request.form['user']
    balance = User.query.filter_by(username=user).first()
    if int(balance.balance) >1000:
        balance.balance = str(int(balance.balance)-1000)
        db.session.commit()
        flash("flag is flag{d0_n0t_s7ea1_fr0m_SPbCTF_cru3l_ARSIB}")
        return redirect(url_for('index'))
    flash("no money no honey")
    return redirect(url_for('index'))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    signinform = SignInForm()
    if request.method == 'POST':
        em = signinform.email.data
        log = User.query.filter_by(email=em).first()
        if log.password == signinform.password.data:
            current_user = log.username
            session['current_user'] = current_user
            session['user_available'] = True
            return redirect(url_for('dice'))
    return render_template('signin.html', signinform=signinform)


@app.route('/about_user')
def about_user():
    aboutuserform = AboutUserForm()
    if session['user_available']:
        user = User.query.filter_by(username=session['current_user']).first()
        return render_template('about_user.html', user=user, aboutuserform=aboutuserform)
    flash('You are not a Authenticated User')
    return redirect(url_for('signin'))


@app.route('/logout')
def logout():
    session.clear()
    session['user_available'] = False
    return redirect(url_for('signin'))


if __name__ == '__main__':
    app.run()
