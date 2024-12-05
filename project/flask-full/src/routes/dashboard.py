from flask import Blueprint
from src.controllers.dashboardController import index, about, login, register, record, logout, account, accountUpdate

dashboardBp = Blueprint('dashboard', __name__)

dashboardBp.route('/', methods=["GET"])(index)
dashboardBp.route('/about', methods=["GET"])(about)
dashboardBp.route('/login', methods=["GET","POST"])(login)
dashboardBp.route('/register', methods=["GET"])(register)
dashboardBp.route('/record', methods=["POST"])(record)
dashboardBp.route('/logout', methods=["GET"])(logout)
dashboardBp.route('/account', methods=["GET"])(account)
dashboardBp.route('/account-update', methods=["POST"])(accountUpdate)