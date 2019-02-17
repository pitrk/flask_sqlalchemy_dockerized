from flask import Flask

from .db import db
from .models import ExampleModel
from .views import router


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    with app.app_context():
        db.init_app(app)
        db.create_all()
        db.session.commit()
        app.register_blueprint(router)
    return app
