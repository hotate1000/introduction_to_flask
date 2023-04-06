from flask import Flask;

app = Flask(__name__);


@app.route("/")
def index():
    return "Hello World!";


@app.route("/hello/<name>", methods=["GET"], endpoint="hello-endpoint")
def hello(name):
    return f"Hello {name}";
