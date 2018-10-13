"""
  Created by Even on 2018-10-13
"""

from flask import Flask, render_template

app = Flask("__main__")


@app.route("/", methods=["POST", "GET"])
def index():
    user = {'name': 'Even'}
    return render_template('index.html', user=user)


@app.route("/home")
def home():

    return "欢迎到家！"



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5005)