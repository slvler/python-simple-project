from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from markupsafe import escape
from flask_bcrypt import Bcrypt
# from flask_sqlalchemy import SQLAlchemy
import pymysql

APP = Flask(__name__)

APP.config['SECRET_KEY'] = "222559999888"

connection = pymysql.connect(
    host='localhost',
    user='newuser',
    password='newpassword',
    database='book',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

bcrypt = Bcrypt()


@APP.route('/')
def index():
    cursor = connection.cursor()
    user_query = "SELECT * FROM user"
    cursor.execute(user_query)
    results = cursor.fetchall()

    posts_query = "SELECT * FROM post"
    cursor.execute(posts_query)
    post_result = cursor.fetchall()

    return render_template('index.html', users=results, posts=post_result)

@APP.route('/test/<test_keyword>')
def test_user(test_keyword):
    return 'current %s' % escape(test_keyword)

@APP.route('/login')
def login():
    return render_template('login.html')

@APP.route('/user/edit/<user_id>')
def user_edit(user_id):
    cursor = connection.cursor()
    sql = "SELECT * FROM user where id = %s"
    cursor.execute(sql, (
        user_id
    ))
    user = cursor.fetchone()
    if not user:
        return redirect(url_for('index'))

    return render_template('edit.html', user=user)

@APP.route('/user/update', methods=['POST'])
def user_update():
    print(request.form)
    cursor = connection.cursor()
    sql = "SELECT * FROM user WHERE id = %s"
    cursor.execute(sql, (
        request.form['id']
    ))
    user = cursor.fetchone()
    if user:
        sql = "UPDATE user SET fullname = %s, surname = %s, email = %s, gender = %s WHERE id = %s"
        cursor.execute(sql, (
            request.form['fullname'],
            request.form['surname'],
            request.form['email'],
            request.form['gender'],
            request.form['id']
        ))
        connection.commit()
        return redirect(url_for('index'))
    else:
        return "error"
        pass


@APP.route('/check', methods=['POST'])
def check():
    cursor = connection.cursor()
    sql = "SELECT * FROM user where email = %s"
    cursor.execute(sql, (
        request.form.get('email')
    ))
    user = cursor.fetchone()
    if user:
        if bcrypt.check_password_hash(user['password'], request.form.get('password')):
            session['user_id'] = user['id']
            session['account'] = True
            return redirect(url_for('index'))
    else:
        return "error"
        pass

@APP.route('/delete/<user_id>')
def delete(user_id):
    cursor = connection.cursor()
    sql = "DELETE FROM user WHERE id = %s"
    cursor.execute(sql, (
        user_id
    ))
    connection.commit()

    if cursor.rowcount > 0:
        return jsonify({'success': 'Delete'})
    else:
        return jsonify({'error': 'Error'}), 404


@APP.route('/register')
def register():
    return render_template('register.html')

@APP.route('/record', methods=['POST'])
def record():
    if request.form['fullname'] and\
            request.form['surname'] and\
            request.form['email'] and\
            request.form['gender'] and\
            request.form['password']:

        sql = "INSERT INTO `user` (`fullname`, `surname`, `email`, `gender`, `password`) VALUES (%s, %s, %s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(sql, (
            request.form.get('fullname'),
            request.form.get('surname'),
            request.form.get('email'),
            request.form.get('gender'),
            bcrypt.generate_password_hash(request.form.get('password')).decode('utf-8'),
        ))
        connection.commit()


    return redirect(url_for('register'))


@APP.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@APP.route('/account')
def account():
    session.clear()
    return redirect(url_for('index'))

@APP.errorhandler(404)
def error_handler_404(error):
    return "<h1>404</h1>"


if __name__ == '__main__':
    APP.debug=True
    APP.run()