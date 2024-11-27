import os
from . import db
import jwt
import datetime
from src.controllers import login_manager
from flask_login import UserMixin



@login_manager.user_loader
def user_loader(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)


    def get_reset_token(self, expiration=36000):
        reset_token = jwt.encode(
            {
                "confirm": self.id,
                "exp": datetime.datetime.now(tz=datetime.timezone.utc)
                       + datetime.timedelta(seconds=expiration)
            },
            os.environ.get('SECRET_KEY'),
            algorithm="HS256"
        )
        return reset_token



    def confirm(self, token):
        try:
            data = jwt.decode(
                token,
                os.environ.get('SECRET_KEY'),
                leeway=datetime.timedelta(seconds=10),
                algorithms=["HS256"]
            )
        except:
            return False
        print(data)
        print(self.id)

        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    @staticmethod
    def verify_reset_token(token):
        s = Serializer("f9bf78b9a18ce6d46a0cd2b0b86df9da")
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}', '{self.password}')"
