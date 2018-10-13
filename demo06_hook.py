"""
  Created by Even on 2018-10-13
"""

from flask import Flask, render_template, make_response

app = Flask("__main__")


@app.route("/", methods=["POST", "GET"])
def index():
    # a = 10 / 0
    user = {'name': 'Even'}
    return render_template('index.html', user=user)


@app.route("/home")
def home():
    return "欢迎到家！"


count = 8


@app.before_first_request
def handle_first_request():
    global count
    count = 1
    print("In before first request func")


@app.before_request
def handle_before_request():
    print("In before request func")


@app.after_request
def handle_after_request(response):
    global count
    response = make_response("你获得的优惠券是%d折的" % count)
    count = 8
    print("In after request func")
    return response


@app.teardown_request
def handle_teardown(response):
    print("In teardown func")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)