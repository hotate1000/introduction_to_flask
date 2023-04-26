from flask import Blueprint, render_template;


detector = Blueprint(
    "detector",
    __name__,
    template_folder="templates"
);


@detector.route("/")
def index():
    return render_template("detector/index.html");
