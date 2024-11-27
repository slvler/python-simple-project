from flask_bcrypt import Bcrypt
import flask_login
from flask_mail import Message, Mail

bcrypt = Bcrypt()
mail = Mail()

login_manager = flask_login.LoginManager()
