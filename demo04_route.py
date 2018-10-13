"""
  Created by Even on 2018-10-13
"""
from flask import Flask, jsonify, render_template, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


@app.route("/", endpoint="sayhello", methods=["GET"])
def hello1():
    return "Hello 1"


@app.route("/", methods=["POST"])
def hello2():
    return "Hello 2"


@app.route("/index")
def index():
    url = url_for("sayhello")
    return redirect(url)



@app.route("/goods/<int:good_id>")
def get_goods(good_id):

    return "Good id is %s" % good_id


class PhoneNumberConverter(BaseConverter):
    def __init__(self, map, regex):
        super().__init__(map)
        self.regex = regex

    def to_python(self, value):
        return "13000000000"

    def to_url(self, value):
        return "100"



app.url_map.converters['re'] = PhoneNumberConverter


@app.route("/<re(r'1[3578]\d{9}'):phone_number>")
def call_sb(phone_number):
    return "Call to %s" % phone_number


@app.route("/home")
def home():
    url = url_for('call_sb', phone_number="13012345678")
    return redirect(url)



if __name__ == "__main__":
    app.run(debug=True)