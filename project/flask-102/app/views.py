from flask import Flask, render_template, redirect, url_for, request, make_response, session
from itsdangerous import Signer
from .session_interface import MySessionInterface

app = Flask(__name__)

app.secret_key = b"014asdasdasD__"
#app.session_interface = MySessionInterface()

@app.route("/")
def index():
    return render_template('main.html')

@app.route("/generic")
def generic():
    return render_template('generic.html')

@app.route("/elements")
def elements():
    return render_template('elements.html')

@app.route("/response")
def response():

    signer = Signer(b"secret key")
    signed_name = signer.sign(b"Mehmet")

    signed_name_str = signed_name.decode()

    response = make_response("<html><body><h1>test response</h1></body></html>")
    response.set_cookie('name', signed_name_str)
    return response


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/hello-admin")
def helloAdmin():
    return render_template('admin.html')


@app.route("/user/<name>")
def user(name):
    if name.lower() == "admin":
        return redirect(url_for("helloAdmin"))
    print(name)
    return render_template('user.html', name=name)


@app.route("/add/<int:number1>/<int:number2>")
def add(number1, number2):
    calculate = number1 + number2
    return render_template('calculate.html', number1=number1, number2=number2, calculate=calculate)


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/login/check", methods=["POST"])
def loginCheck():
    name = request.form.get('name')
    password = request.form.get('password')
    print(request.form)
    result = "name: {}, password: {}".format(name, password)
    return result


@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/record", methods=["POST"])
def record():
    context = {
        'email': request.form.get('email'),
        'password': request.form.get('password'),
        'rePassword': request.form.get('re-password'),
        'role': request.form.get('role')
    }
    print(context)
    return render_template('record.html', **context)


@app.route("/argument")
def argument():
    print(request.args)
    name = request.args["name"]
    surname = request.args["surname"]
    print(name + " " + surname)
    return "argument"
