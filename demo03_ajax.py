"""
  Created by Even on 2018-10-13
"""
# import json

from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("ajax.html")

@app.route('/userinfo')
def get_user_info():
    data = {"name": "Alice", "height": 180}
    return jsonify(data)
    # data = {"name": "Alice"}
    # data = json.dumps(data)
    # print(data) headers
    # return data, 200, {'Content-Type': "application/json"}


if __name__ == "__main__":
    app.run(debug=True)