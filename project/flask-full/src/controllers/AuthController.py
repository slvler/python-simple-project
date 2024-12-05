from flask import redirect, url_for, render_template, flash
from flask_login import current_user
from src.forms.RequestResetForm import RequestResetForm, UpdatePasswordForm
from src.models.user import User
from flask_mail import Message
from . import mail

def send_reset_mail(user):
    token = user.get_reset_token()
    msg = Message(
        subject='Password Reset Request',
        sender="demo@demo.com",
        recipients=[user.email])
    msg.body = f'''To reset you password, visit the following link: {url_for(('auth.reset'), token=token, _external=True)}
    If you did not make this request then simply ignore this email and no change
    '''
    mail.send(msg)


def reset_password():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.index"))
    form = RequestResetForm()
    print(form.data)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_mail(user)
        flash('send mail')
        return redirect(url_for('dashboard.login'))

    return render_template('auth/reset_request.html', form=form)


def reset(token):
    # if current_user.is_authenticated:
    #     return redirect(url_for("dashboard.index"))

    user = User()
    control = user.confirm(token=token)
    if not control:
        flash(f'error')
        return redirect(url_for('dashboard.index'))
    form = UpdatePasswordForm()
    return render_template('auth/reset_token.html', form=form)


def clear_password():
    return "111"