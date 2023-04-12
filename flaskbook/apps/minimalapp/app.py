from flask import Flask, render_template, url_for, redirect, request, flash;
from email_validator import validate_email, EmailNotValidError;
# from flask import current_app, g, request;


app = Flask(__name__);
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ";


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


@app.route("/contact")
def contact():
    return render_template("contact.html");


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        username = request.form["username"];
        email = request.form["email"];
        description = request.form["description"];

        is_valid = True;

        if not username:
            flash("ユーザ名は必須です。");
            is_valid = False;

        if not email:
            flash("メールアドレスは必須です。");
            is_valid = False;

        try:
            validate_email(email);
        except EmailNotValidError:
            flash("メールアドレスの形式で入力してください。");
            is_valid = False;

        if not description:
            flash("問い合わせ内容は必須です。");
            is_valid = False;

        if not is_valid:
            return redirect(url_for("contact"));

        flash("問い合わせ内容はメールにて送信しました。問い合わせありがとうございます。");

        # メールを送る（最後に実装）
        return redirect(url_for("contact_complete"));
    return render_template("contact_complete.html");
