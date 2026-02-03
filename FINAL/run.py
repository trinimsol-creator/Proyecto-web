# https://flask.palletsprojects.com/en/2.3.x/
# https://pythonbasics.org/flask-http-methods/

from flask import Flask

app = Flask(__name__)

from route import route
route(app)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)
