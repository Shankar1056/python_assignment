from student import app, Students
from flask import render_template


@app.route("/login/<id>")
def login_hey(id):
    # all_users = Users.query.all()    ----  to get all the values from the DB

    # users = Students.query.filter_by(email='manjunath@test.com').all()  # --- to get users by specific condition
    us = Students.query.filter_by(id=id).first()  # --- to select a particular user by specific condition


    return render_template("login.html", username=us.name)
