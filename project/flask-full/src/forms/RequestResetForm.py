from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo
from src.models.user import User


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if not email:
            raise ValidationError('That email is taken. Please choose a different one')


class UpdatePasswordForm(FlaskForm):
    password = StringField('Password', validators=[DataRequired(message="Password required")])
    confirm_password = StringField('Confirm Password', validators=[DataRequired(message="Confirm required"), EqualTo('password')])
    submit = SubmitField('Request Password Reset')