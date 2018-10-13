"""
  Created by Even on 2018-10-13
"""
from flask import Flask, render_template, abort, make_response

app = Flask(__name__)


@app.route("/")
def index():
    # abort(200)
    response = make_response("Hello", 404, {'location': 'http://www.baidu.com'})
    return response


if __name__ == "__main__":
    app.run(debug=True)