from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456789@127.0.0.1:3306/swapi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class People(db.Model):
    __tablename__ = "people"

    ssn = db.Column("ssn", db.Integer, primary_key=True)
    firstname = db.Column("firstname", db.String(255))
    lastname = db.Column("lastname", db.String(255))
    gender = db.Column("gender", db.CHAR)
    age = db.Column("age", db.Integer)

    def __init__(self, snn, firstname, lastname, gender, age):
        self.ssn = snn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age


@app.route('/')
def index():
    all_data = db.paginate(db.select(People).order_by(People.ssn))
    # all_data = People.query.all()
    return render_template('index.html', people=all_data)


@app.route('/create')
def create():
    return render_template('create.html')


@app.route("/store", methods=["POST"])
def store():
    ssn = request.form['ssn']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    gender = request.form['gender']
    age = request.form['age']

    new_people = People(snn=ssn,firstname=firstname,lastname=lastname,gender=gender,age=age)

    try:
        db.session.add(new_people)
        db.session.commit()
        return redirect('/')
    except:
        return "Fail"


@app.route('/delete/<int:ssn>')
def delete(ssn):
    people_delete = People.query.filter_by(ssn=ssn).first()

    try:
        db.session.delete(people_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "Fail"


@app.route('/edit/<int:ssn>', methods=["GET"])
def edit(ssn):
    people_edit = People.query.filter_by(ssn=ssn).first()
    return render_template('edit.html', people=people_edit)


@app.route('/update/<int:ssn>', methods=["POST"])
def update(ssn):
    people_update = People.query.filter_by(ssn=ssn).first()
    people_update.firstname = request.form['firstname']
    people_update.lastname = request.form['lastname']
    people_update.gender = request.form['gender']
    people_update.age = request.form['age']

    try:
        db.session.commit()
        return redirect('/')
    except:
        return "FAİL"



if __name__ == "__main__":
    app.run(debug=True)
