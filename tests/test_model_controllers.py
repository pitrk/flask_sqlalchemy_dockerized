from flask_testing import TestCase

from application.model_controllers import ExampleModelController
from application import create_app
from application.db import db

from .configuration import FlaskTestConfig


class TestModelControllers(TestCase):
    def create_app(self):
        app = create_app(FlaskTestConfig)
        return app

    def setUp(self):
        self.controller = ExampleModelController()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_len_counts_ports_correctly(self):
        self.assertEqual(0, len(self.controller))
        self.controller.add('one')
        self.assertEqual(1, len(self.controller))
