from flask import render_template

def route(app):

    @app.route("/")
    def home():
        return render_template("PPrincipal.html")
