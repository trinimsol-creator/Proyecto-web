# https://flask.palletsprojects.com/en/2.3.x/
# https://pythonbasics.org/flask-http-methods/

import os

from flask import Flask, session

app = Flask(__name__)

from route import route
route(app)

app.secret_key = "super_clave_secreta_123"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True, use_reloader=False)

