import os
from functools import wraps
from flask import Flask, send_file, request, make_response, session, redirect, url_for, render_template, abort, flash, jsonify
from werkzeug.utils import secure_filename

from config import config


app = Flask(__name__)
app.config.from_object(config)

app.secret_key = os.getenv('SECRET_KEY').encode()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not "user" in session.keys():
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def get_password(user):
    return open(os.path.join(config["auth_dir"], user), "r", encoding="utf-8").read()


def set_password(user, password):
    return open(os.path.join(config["auth_dir"], user), "w+", encoding="utf-8").write(password)


def user_exists(user):
    return os.path.exists(os.path.join(config["auth_dir"], user))


def dir_exists(user, directory):
    return os.path.exists(os.path.join(config["storage_dir"], user, directory))


def create_dir(user, directory):
    return os.makedirs(os.path.join(config["storage_dir"], user, directory))


def path_for(user, filename):
    return os.path.join(config["storage_dir"], user, filename)


def list_dir(user, dirpath=""):
    return os.listdir(os.path.join(config["storage_dir"], user, dirpath))


@app.route("/")
def index():
    if not "user" in session:
        return redirect(url_for("login_page"))
    return render_template("index.html", tree=list_dir(session["user"]))


@app.route("/login")
def login_page():
    return render_template("login.html")


@app.route("/api/signup", methods=["POST"])
def signup():
    user = request.form["user"]
    password = request.form["password"].strip()

    if user_exists(user):
        return redirect(url_for("login_page"))

    set_password(user, password)
    create_dir(user, ".")
    session["user"] = user
    return redirect(url_for("index"))


@app.route("/api/login", methods=["POST"])
def login():
    user = request.form["user"]
    password = request.form["password"].strip()

    true_password = ""

    try:
        true_password = get_password(user)
    except:
        return redirect(url_for("login"))

    if true_password == password:
        session["user"] = user
        return redirect(url_for("index"))
    else:
        return redirect(url_for("login_page"))


@app.route("/api/upload", methods=["PUT", "POST"])
@login_required
def upload():
    f = request.files['file']
    f.save(os.path.join(config['storage_dir'],
                        session["user"], secure_filename(f.filename)))
    return redirect(url_for('index'))


@app.route("/api/mkdir", methods=["PUT", "POST"])
@login_required
def mkdir():
    directory = request.form['dir']

    if directory.count("..") >= 2:
        return render_template("error.html", error="Sorry bro")

    if dir_exists(session["user"], directory):
        return redirect(url_for("index"))

    create_dir(session["user"], directory)
    return redirect(url_for("index"))


@app.route("/api/read", methods=["POST"])
@login_required
def readfile():
    filename = request.form['filename']

    if filename.count("..") >= 2:
        return render_template("error.html", error="Sorry bro")

    if not os.path.exists(path_for(session["user"], filename)):
        flash('No such file', 'error')
        return redirect(url_for("index"))
    if os.path.isdir(path_for(session["user"], filename)):
        return render_template("error.html", error="It's a dir, bro")
    return send_file(path_for(session["user"], filename))


@app.route("/api/tree", methods=["POST"])
@login_required
def tree():
    dirpath = request.form["dirpath"] or ""

    if dirpath.count("..") >= 2:
        return render_template("error.html", error="Sorry bro")

    return jsonify(list_dir(session["user"], dirpath))
