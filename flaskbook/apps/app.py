from flask import Flask;
from apps.crud import views as crud_views;
# from pathlib import Path;
from flask_migrate import Migrate;
from apps.app2 import db;
from flask_wtf.csrf import CSRFProtect;
from apps.config import config;


csrf = CSRFProtect();


def create_app(config_key):
    app = Flask(__name__);
    app.config.from_object(config[config_key]);
    # app.config.from_mapping(
    #     SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
    #     SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
    #     SQLALCHEMY_TRACK_MODIFICATIONS=False,
    #     # sqlの結果をコンソールに出力
    #     SQLALCHEMY_ECHO=True,
    #     WTF_CSRF_KEY="AuwzyszU5sugKN7KZs6f",
    # )
    csrf.init_app(app);
    db.init_app(app);
    Migrate(app, db);
    app.register_blueprint(crud_views.crud, url_prefix="/crud");
    return app;
