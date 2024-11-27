import os
from flask import Flask
from flask_mail import Mail, Message
from src.routes.dashboard import dashboardBp
from src.routes.PostRoute import PostBp
from src.routes.auth import AuthBp
from src.models import db
from src.controllers import Bcrypt, login_manager


def create_app():
    app = Flask(__name__)

    app.register_blueprint(dashboardBp, url_prefix='/')
    app.register_blueprint(PostBp, url_prefix='/post')
    app.register_blueprint(AuthBp, url_prefix='/auth')

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = '#'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

    db.init_app(app)
    Bcrypt(app)

    login_manager.init_app(app)
    login_manager.login_view = 'dashboard.login'
    login_manager.login_message_category = 'info'


    app.config['MAIL_SERVER'] = '#'
    app.config['MAIL_PORT'] = 999999
    app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
    app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False

    with app.app_context():
        from src.models.user import User
        from src.models.post import Post
        db.create_all()

    Mail(app)

    return app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)