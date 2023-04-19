from flask import Flask;
from apps.crud import views as crud_views;
from pathlib import Path;
from flask_migrate import Migrate;
from flask_sqlalchemy import SQLAlchemy;


# def create_app():
app = Flask(__name__);
app.register_blueprint(crud_views.crud, url_prefix="/crud");

db = SQLAlchemy();

app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ";
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}";
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False;

db.init_app(app);
Migrate(app, db);
