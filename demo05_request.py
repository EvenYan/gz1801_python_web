"""
  Created by Even on 2018-10-13
"""
from flask import Flask, request, render_template, redirect, make_response, url_for, g
from werkzeug.routing import BaseConverter

app = Flask(__name__)

u = None
p = None

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form.getlist("username")
        passwd = request.form.get("passwd")
        print(name, passwd)
        global u
        u = name
        global p
        p = passwd
        return redirect(url_for("index"))
    return render_template("login.html")


@app.route("/index")
def index():
    user = u
    passwd = p
    return render_template("index.html", user=user)


@app.route("/goods")
def deal_goods():
    username = request.args.getlist("name")
    print(username)

    return "username: %s" % username


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("pic")
    print(file)
    file.save("./test.png")
    return "上传成功"


@app.route("/gdemo")
def func():
    a = [1, 2, 3]
    g.a = a
    total = sum1()
    return "total: %s" % total


def sum1():
    a = g.a
    b = g.a
    return sum(a)


@app.route("/home")
def home():
    g.a
    return "hello"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")