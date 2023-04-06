from flask import Flask;
from flask import render_template;

app = Flask(__name__);


@app.route("/")
def index():
    return "Hello World!";


@app.route("/hello/<name>",
           methods=["GET"],
           endpoint="hello-endpoint")
def hello(name):
    return f"Hello {name}";


@app.route("/name/<name>")
def show_name(name):
    # name=nameはname変数をviewに渡している
    return render_template("index.html", name=name);
