from flask_api import status
from flask_testing import TestCase

from application import create_app
from application.db import db

from .configuration import FlaskTestConfig


class TestViews(TestCase):
    def create_app(self):
        app = create_app(FlaskTestConfig)
        return app

    def setUp(self):
        app = create_app(FlaskTestConfig)
        self.test_app = app.test_client()
        self.test_app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_home_page(self):
        result = self.test_app.get('/')
        self.assertEqual(result.status_code, status.HTTP_200_OK)
