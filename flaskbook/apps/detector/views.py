from flask import Blueprint, render_template;
from apps.crud.models import db, User;
from apps.detector.models import UserImage;


detector = Blueprint(
    "detector",
    __name__,
    template_folder="templates"
);


@detector.route("/")
def index():
    user_images = (
        db.session.query(User, UserImage)
        .join(UserImage)
        .filter(User.id == UserImage.user_id)
        .all()
    )
    return render_template("detector/index.html", user_images=user_images);
