from flask import Flask;
from apps.crud import views as crud_views;
from pathlib import Path;
from flask_migrate import Migrate;
from apps.app2 import db;
# from flask_sqlalchemy import SQLAlchemy;
# from datetime import datetime;
# from werkzeug.security import generate_password_hash;


# db = SQLAlchemy();


def create_app():
    app = Flask(__name__);
    app.config.from_mapping(
        SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        # sqlの結果をコンソールに出力
        SQLALCHEMY_ECHO=True
    )
    db.init_app(app);
    Migrate(app, db);
    app.register_blueprint(crud_views.crud, url_prefix="/crud");
    return app;


# class User(db.Model):
#     __tablename__ = "users";

#     id = db.Column(db.Integer, primary_key=True);
#     username = db.Column(db.String, index=True);
#     email = db.Column(db.String, unique=True, index=True);
#     password_hash = db.Column(db.String);
#     created_at = db.Column(db.DateTime, default=datetime.now);
#     updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now);

#     @property
#     def password(self):
#         raise AttributeError("読み取り不可");

#     @password.setter
#     def password(self, password):
#         self.password_hash = generate_password_hash(password);
