from flask import Flask;
from apps.crud import views as crud_views;
from apps.auth import views as auth_views;
from flask_migrate import Migrate;
from apps.crud.models import db, csrf, login_manager;
from apps.config import config;


login_manager.login_view = "auth.signup";
login_manager.login_message = "";


def create_app(config_key):
    app = Flask(__name__);
    app.config.from_object(config[config_key]);
    csrf.init_app(app);
    db.init_app(app);
    Migrate(app, db);
    login_manager.init_app(app);
    app.register_blueprint(crud_views.crud, url_prefix="/crud");
    app.register_blueprint(auth_views.auth, url_prefix="/auth");
    return app;
