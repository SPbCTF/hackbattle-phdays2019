import mysql.connector
import os.path
import random

IMAGES_ROOT = '/var/www/uploads'

def _get_conn():
    return mysql.connector.connect(user='imgstore', database='imgstore', unix_socket='/var/run/mysqld/mysqld.sock')

def _gen_fname():
    return ''.join(random.choice('0123456789abcdef') for _ in xrange(32))

class UserNotFound(Exception):
    pass

class InvalidPassword(Exception):
    pass

class ImageNotFound(Exception):
    pass

class User(object):
    def __init__(self, login, password):
        self.login = login
        self.password = password

# TODO: add create_user

def get_user(login, password):
    conn = _get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT login, password FROM users WHERE login='{}'".format(login))
        res = cursor.fetchone()
        if res:
            db_user = User(*res)
            if db_user.password != password:
                raise InvalidPassword('Invalid password for user "{}"'.format(db_user.login))
            return db_user
        else:
            raise UserNotFound('User not found')
    finally:
        conn.close()

def store_image(user, image):
    fname = _gen_fname()
    conn = _get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO images (login, fname) VALUES ('{}', '{}')".format(user.login, fname))
        image.save(os.path.join(IMAGES_ROOT, fname))
        conn.commit()
    finally:
        conn.close()

def list_images(user):
    conn = _get_conn()
    try:
        cursor = conn.cursor()
        query = 'SELECT fname FROM images'
        if user.login != 'admin':
            query += " WHERE login='{}'".format(user.login)
        cursor.execute(query)
        return [r[0] for r in cursor]
    finally:
        conn.close()

def get_image(user, fname):
    if user.login != 'admin' and fname not in list_images(user):
        raise ImageNotFound('Image not found')

    path = os.path.join(IMAGES_ROOT, fname)
    if not os.path.exists(path):
        raise ImageNotFound('Image "{}" not found'.format(fname))
    with open(path, 'rb') as img:
        return img.read()
