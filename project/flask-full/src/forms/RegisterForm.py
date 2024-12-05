from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from src.models.user import User

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Kullanıcı adı gereklidir.")])
    email = StringField('Email', validators=[DataRequired(message="Kullanıcı adı gereklidir."), Email()])
    password = StringField('Password', validators=[DataRequired(message="Kullanıcı adı gereklidir.")])
    confirm_password = StringField('Confirm Password', validators=[DataRequired(message="Kullanıcı adı gereklidir."), EqualTo('password')])
    submit = SubmitField('Sing Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is taken. Please choose a different one')