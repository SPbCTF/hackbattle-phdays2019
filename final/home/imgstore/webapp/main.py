from flask import *
import db

app = Flask("ImgStore")

@app.errorhandler(db.UserNotFound)
def user_not_found(error):
    return str(error), 404

@app.errorhandler(db.InvalidPassword)
def invalid_password(error):
    return str(error), 403

@app.errorhandler(db.ImageNotFound)
def image_not_found(error):
    return str(error), 404

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/upload', methods=['POST'])
def upload():
    user = db.get_user(request.args['login'], request.args['password'])
    db.store_image(user, request.files['image'])
    return 'Uploaded successfully'

@app.route('/list')
def list():
    user = db.get_user(request.args['login'], request.args['password'])
    return '\n'.join(db.list_images(user))

@app.route('/get')
def get():
    user = db.get_user(request.args['login'], request.args['password'])
    return db.get_image(user, request.args['image']), 200, {'Content-Type': 'application/octet-stream'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=20001, debug=False)
