from flask import Flask, render_template, url_for;
# from flask import current_app, g, request;

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


with app.test_request_context():
    print(url_for("index"));
    print(url_for("hello-endpoint", name="world"));
    print(url_for("show_name", name="ichiro", page="1"));


# ctx = app.app_context();
# ctx.push();

# print(current_app.name);

# g.connection = "connection";
# print(g.connection);


# with app.test_request_context("/users?updated=true"):
#     print(request.args.get("updated"));