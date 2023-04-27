import uuid;
from flask import (
    Blueprint,
    current_app,
    render_template,
    send_from_directory,
    redirect,
    url_for
)
from apps.crud.models import db, User;
from apps.detector.models import UserImage;
from pathlib import Path;
from apps.detector.forms import UploadImageForm;
from flask_login import current_user, login_required;


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


@detector.route("/images/<path:filename>")
def image_file(filename):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], filename);


@detector.route("/upload", methods=["GET", "POST"])
@login_required
def upload_image():
    form = UploadImageForm();
    if form.validate_on_submit():
        file = form.image.data;
        ext = Path(file.filename).suffix;
        image_uuid_file_name = str(uuid.uuid4()) + ext;

        # 画像を保存する。
        image_path = Path(
            current_app.config["UPLOAD_FOLDER"], image_uuid_file_name
        );
        file.save(image_path);

        # DBに保存する。
        user_image = UserImage(
            user_id=current_user.id, image_path=image_uuid_file_name
        );
        db.session.add(user_image);
        db.session.commit();

        return redirect(url_for("detector.index"));
    return render_template("detector/upload.html", form=form);
