from student import app, Students
from flask import render_template


@app.route("/allusers")
def all_users():
    allusers = Students.query.all()  # --- get all the values from the DB
    return render_template("all_users.html", users=allusers)
