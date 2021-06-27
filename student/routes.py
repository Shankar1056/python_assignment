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

    # users = Students.query.filter_by(email=userEmail).first()
    # if users:
    #  flash('Email address already exists',' error')

    #  return render_template("signup.html")

    new_user = Students(username=userName, email=userEmail, password=userPassword)
    db.session.add(new_user)
    db.session.commit()

    return render_template("login.html")

# Login
@app.route("/login", methods=['GET', 'POST'])
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

    allusers = Students.query.all()  # --- get all the values from the DB
    return render_template("all_students.html", users=allusers)


# to delet the user based on ID
@app.route("/delete/<id>")
def delete(id):
    # logic
    print(id)
    db.session.query(Students).filter(Students.id == id).delete()
    db.session.commit()
    print("success")


# to update the user based on ID
@app.route("/update/<id>")
def update(id):
    # logic
    admin = Students.query.filter_by(id=id).first()
    admin.username = 'Daya Shankar'
    db.session.commit()
