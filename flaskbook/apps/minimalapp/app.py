# $env:FLASK_APP="apps.minimalapp.app.py"
# $env:FLASK_ENV="development"
# $env:FLASK_DEBUG="1"
# Flaskクラスをimport
from flask import Flask;

app = Flask(__name__);
# print(app.config);


@app.route("/")
def index():
    return "Hello, World!";
