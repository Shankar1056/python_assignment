from werkzeug.utils import redirect

from student import app, Students, db
from flask import request, render_template, Blueprint, flash

usercontrol = Blueprint("usercontrol", __name__)


# Signup
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    # logic
    if request.method == 'GET':
        return render_template("signup.html")

    data = request.form
    userName = data['username']
    userEmail = data['email']
    userPassword = data['password']

    users = Students.query.filter_by(email=userEmail).first()
    if users:
        flash('Email address already exists', ' error')

        return render_template("signup.html")

    new_user = Students(username=userName, email=userEmail, password=userPassword)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/")


# Login
@app.route("/", methods=['GET', 'POST'])
def login():
    # logic
    if request.method == 'GET':
        return render_template("login.html")

    data = request.form
    userEmail = data['email']
    userPassword = data['password']

    # users = Students.query.filter_by(email=userEmail).first()
    # if not users:
    # flash('Please check Email and try again.')
    # return render_template("login.html")

    userDetails = Students.query.filter_by(email=userEmail).first()  # --- get user details from the DB
    print(userDetails.username)
    return render_template("/user_details.html", users=userDetails)


# to delet the user based on ID
@app.route("/display")
def displayAllUsers():
    # logic
    allusers = Students.query.all()  # --- get all the values from the DB
    # print(allusers.email)
    return render_template("all_students.html", users=allusers)


# to delet the user based on ID
@app.route("/delete/")
def delete():
    # logic

    db.session.query(Students).delete()
    db.session.commit()
    return redirect("/signup")


# to update the user based on ID
@app.route("/update")
def update():
    # logic
    admin = Students.query.filter_by(email="shankar@gmail.com").first()
    admin.username = 'Daya Shankar'
    db.session.commit()
    return redirect("/display")
