from email_validator import validate_email, EmailNotValidError;
from flask import (
    Flask,
    # current_app,
    # g,
    request,
    render_template,
    redirect,
    url_for,
    flash,
);


app = Flask(__name__);
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ";


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

        return redirect(url_for("contact_complete"));
    return render_template("contact_complete.html");
