from flask import Blueprint, render_template;
# from apps.app import User, db;


crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@crud.route("/")
def index():
    return render_template("crud/index.html");


# @crud.route("/sql")
# def sql():
#     db.session.query(User).all();
#     return "コンソールログに表示";
