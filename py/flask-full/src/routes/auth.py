from flask import Blueprint
from src.controllers.AuthController import reset_password, reset, clear_password

AuthBp = Blueprint('auth', __name__)

AuthBp.route('/reset_request', methods=["GET", "POST"])(reset_password)
AuthBp.route('/reset/<token>', methods=["GET"])(reset)
AuthBp.route('/reset_password', methods=["POST"])(clear_password)
