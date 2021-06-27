from flask import Flask   # pip install flask
from flask_sqlalchemy import SQLAlchemy  # pip install -U Flask-SQLAlchemy
from sqlalchemy.orm import Session

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
sess = Session()

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:12345678@localhost/student"
                                      # "mysql+pymysql://username:passwd@localhost/databasename"
db = SQLAlchemy(app)


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)

# the below command is to create the table
# from student import db -> student is the folder
# db.creat_all()



# to show th record, below are the steps
# 1. use databasename -> give the database name you want to intract with
# 2. Select * from table name


from student import routes  #example for having all the views in a separate py file
from student import views   #example for having all the views in a separate folder