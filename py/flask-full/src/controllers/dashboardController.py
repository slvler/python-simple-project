import os
import secrets
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required

from src.forms.RegisterForm import RegisterForm
from src.forms.LoginForm import LoginForm
from src.models.user import User
from src.models import db
from src.forms.UpdateAccountForm import UpdateAccountForm
from . import bcrypt
from PIL import Image


def index():
    return render_template("index.html")


def about():
    return render_template("about.html")


def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            flash(f'Logged in!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('dashboard.index'))
        else:
            flash(f'login unsuccessfully','danger')
    return render_template("login.html", form=form)


def register():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.index"))
    form = RegisterForm()
    return render_template("register.html", form=form)


def record():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.index"))

    form = RegisterForm()
    if form.validate_on_submit():
        password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data,email=form.email.data,password=password)

        db.session.add(new_user)
        db.session.commit()

        flash(f'successfully account create', 'success')
        return redirect(url_for('dashboard.index'))

    return render_template("register.html", form=form)

def logout():
    logout_user()
    return redirect(url_for('dashboard.index'))


@login_required
def account():
    form = UpdateAccountForm()
    form.username.data = current_user.username
    form.email.data = current_user.email
    image_file = url_for('static', filename='images/person_1.jpg')
    return render_template('account.html', image_file=image_file, form=form)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)

    picture_fn = random_hex + f_ext
    picture_path = os.path.join('static', 'profile_pics', picture_fn)

    out_put_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(out_put_size)
    i.save(picture_path)

    #form_picture.save(picture_path)

    return picture_fn

@login_required
def accountUpdate():
    form = UpdateAccountForm()
    print(form.data)
    if form.validate_on_submit():

        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f'account updated')
        return redirect(url_for('dashboard.account'))
    return render_template("account.html", form=form)