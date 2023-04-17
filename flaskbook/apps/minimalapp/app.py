# Flaskクラスをimport
from flask import Flask, render_template, url_for, current_app, g, request, redirect;


app = Flask(__name__);
# print(app.config);


@app.route("/")
def index():
    return "Hello, World!";


@app.route("/hello/<name>",
           methods=["GET", "POST"],
           endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}";


@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name);


with app.test_request_context():
    # url_forの動作確認
    print(url_for("index"));
    # nameは変数
    print(url_for("hello-endpoint", name="world"));
    print(url_for("show_name", name="ichiro", page="1"));


@app.route("/contact")
def contact():
    return render_template("contact.html");


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        return redirect(url_for("contact_complete"));
    return render_template("contact_complete.html");
