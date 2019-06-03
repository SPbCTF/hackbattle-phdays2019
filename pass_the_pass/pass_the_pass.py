import os
from functools import wraps
from flask import Flask, send_file, request, make_response, session, redirect, url_for, render_template, abort, flash, jsonify
from werkzeug.utils import secure_filename

from config import config

flag = "flag{Th3_Do0rs_oF_Dur1n_L0rD_0f_|\/|or14_5p34k_fr1eNd_aNd_3nT3r}"

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
    return open(os.path.join(os.getcwd(), config["auth_dir"], user), "r", encoding="utf-8").readline()

def get_admin(user):
    return int(open(os.path.join(os.getcwd(), config["auth_dir"], user), "r", encoding="utf-8").readline().readline())


def set_password(user, password, isadmin):
    return open(os.path.join(os.getcwd(), config["auth_dir"], user), "w+", encoding="utf-8").write(password + '\n' + str(isadmin))


def user_exists(user):
    return os.path.exists(os.path.join(os.getcwd(),config["auth_dir"], user))


def dir_exists(user, directory):
    return os.path.exists(os.path.join(os.getcwd(),config["storage_dir"], user, directory))


def create_dir(user, directory):
    return os.makedirs(os.path.join(os.getcwd(), config["storage_dir"], user, directory))


def path_for(user, filename):
    return os.path.join(os.getcwd(),config["storage_dir"], user, filename)


def list_dir(user, dirpath=""):
    return os.listdir(os.path.join(os.getcwd(), config["storage_dir"], user, dirpath))


@app.route("/")
def index():
    if not "user" in session:
        return redirect(url_for("login_page"))

    if session["admin"] == 1:
        headerbox = "О, прянички!"
        flagbox = flag
    else:
        headerbox = "Коробка из под пряников"
        flagbox = "Хмм, ты не говорил, что ты admin... Так что тут ничего нет"
    return render_template("index.html",  header=headerbox, flag=flagbox)


@app.route("/login")
def login_page():
    return render_template("login.html")


@app.route("/api/signup", methods=["POST"])
def signup():
    user = request.form["user"]
    password = request.form["password"].strip()
    try:
        admin = int(request.form["admin"])
        print(admin)
    except KeyError:
        admin = int(0)

    if user_exists(user):
        return redirect(url_for("login_page"))

    set_password(user, password, admin)
    create_dir(user, ".")
    session["user"] = user
    session["admin"] = admin
    return redirect(url_for("index"))