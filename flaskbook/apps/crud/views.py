from flask import Blueprint, render_template, redirect, url_for;
from apps.app2 import User;
from apps.app2 import db;
from apps.crud.forms import UserForm;


crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@crud.route("/")
def index():
    return render_template("crud/index.html");


@crud.route("/sql")
def sql():
    print('sql結果の出力');
    print('-------------');
    db.session.query(User).all();
    print('-------------');
    # db.session.query(User).first();
    # db.session.query(User).get(2);
    # db.session.query(User).count();
    return "コンソールログに表示";


@crud.route("/users/new", methods=["GET", "POST"])
def create_user():
    form = UserForm();
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        db.session.add(user);
        db.session.commit();
        return redirect(url_for("crud.users"));
    return render_template("crud/create.html", form=form);


@crud.route("/users")
def users():
    # usersテーブルの情報を取得する
    users = User.query.all();
    return render_template("crud/index.html", users=users);


# methodsにGETとPOSTを指定する
@crud.route("/users/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    form = UserForm();
    # ユーザーを取得する
    user = User.query.filter_by(id=user_id).first();

    if form.validate_on_submit():
        user.username = form.username.data;
        user.email = form.email.data;
        user.password = form.password.data;
        db.session.add(user);
        db.session.commit();
        return redirect(url_for("crud.users"));

    return render_template("crud/edit.html", user=user, form=form);
