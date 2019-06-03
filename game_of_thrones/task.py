from flask import Flask, session, render_template, request, make_response
from flask_session import Session
import glob
import random
import re
import shutil
import os

app = Flask(__name__)
app.secret_key = b'phdays___'

SESSION_TYPE = 'filesystem'
SESSION_USE_SIGNER = True
sess = Session()


@app.route('/')
def entry_point():

    try:
        id = session['id']
    except:
        session['id'] = str(random.randint(100000, 999999))
        id = session['id']

    try:
        score = session['score']
    except:
        session['score'] = 0
        score = session['score']

    try:
        answer = request.values.get('answer')
        print(id, score, answer, session['task'])
        if answer:
            if answer == session['task']:
                session['score'] += 1
            else:
                session['score'] -= 1
    except:
        pass

    images = glob.glob(r'static/*.png')
    task = random.choice(images)

    try:
        shutil.copyfile(task, os.path.join("static", "task", id+'.png'))
    except shutil.SameFileError:
        pass

    session["task"] = re.search('static/(.*)\.png', task).group(1)

    try:
        score = session['score']
    except:
        session['score'] = 0
        score = session['score']

    r = make_response(render_template('index.html', flag="Get 150 or more right answers to get a flag!" if score <
                                      150 else 'Congratz! Flag is: flag{Dr4G0n_dR0p}', dummy=random.randint(10000000, 9999999999999999)))
    return r


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)
    sess.init_app(app)
