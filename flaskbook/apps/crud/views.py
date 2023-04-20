from flask import Blueprint, render_template;
from apps.app2 import User;
from apps.app2 import db;


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
