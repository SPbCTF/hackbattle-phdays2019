from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from app import login

class User(UserMixin):
    def __init__(self, uid, username, pwhash):
        super(User, self).__init__()
        self.uid = uid
        self.username = username
        # Now store hash instead of plaintext password
        self.pwhash = pwhash

    def get_id(self):
        return self.uid

# Add admin user for testing
users = [
    User(uid=0, 
        username='admin',
        pwhash='pbkdf2:sha256:150000$FDzyOFXi$b36cc6fbaa0688fc3d2de2f0f0c5a5d5d7497e070033248ffbfbc729b6aaf890')
]

def get_user_by_name(name):
    for user in users:
        if user.username == name:
            return user
    return None

@login.user_loader
def load_user(id):
    if id < len(users):
        return users[id]
    else:
        return None