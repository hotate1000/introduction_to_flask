from flask import Flask, render_template;
from apps.crud import views as crud_views;
from apps.auth import views as auth_views;
from apps.detector import views as detector_views;
from flask_migrate import Migrate;
from apps.crud.models import db, csrf, login_manager;
from apps.config import config;


login_manager.login_view = "auth.signup";
login_manager.login_message = "";


def create_app(config_key):
    # print(config_key); localと表示。
    app = Flask(__name__);
    app.config.from_object(config[config_key]);
    csrf.init_app(app);
    db.init_app(app);
    Migrate(app, db);
    login_manager.init_app(app);
    app.register_blueprint(crud_views.crud, url_prefix="/crud");
    app.register_blueprint(auth_views.auth, url_prefix="/auth");
    app.register_blueprint(detector_views.detector, url_prefix="/");
    app.register_error_handler(404, page_not_found);
    app.register_error_handler(500, internal_server_error);
    return app;


def page_not_found(e):
    return render_template("404.html"), 404;


def internal_server_error(e):
    return render_template("500.html"), 500;
