import pytest;
import os;
import shutil;
print = os.getcwd();
from apps.app import create_app;
from apps.crud.models import db;
from apps.crud.models import User;
from apps.detector.models import UserImage, UserImageTag;


# @pytest.fixture
# def app_data():
#     return 3;
@pytest.fixture
def fixture_app():
    # テスト用
    app = create_app("testing");
    app.app_context().push();

    with app.app_context():
        db.create_all();

    os.mkdir(app.config["UPLOAD_FOLDER_TEST"]);

    # テストを実行。
    yield app;

    # クリーンアップ、レコードの削除。
    User.query.delete();
    UserImage.query.delete();
    UserImageTag.query.delete();

    # 画像アップロードディレクトリを削除。
    shutil.rmtree(app.config["UPLOAD_FOLDER_TEST"]);

    db.session.commit();


@pytest.fixture
def client(fixture_app):
    return fixture_app.test_client();
