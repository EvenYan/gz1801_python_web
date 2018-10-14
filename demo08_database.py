"""
  Created by Even on 2018-10-13
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, String, Integer
from flask_migrate import Migrate
from flask_script import Manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/gz_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)



class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=True)
    passwd = db.Column(db.String(100), default="abc")


@app.route("/")
def index():
    return "Hello Flask!"


if __name__ == "__main__":
    manager.run()
    # db.drop_all()
    # db.create_all()