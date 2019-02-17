import sqlite3

from sqlalchemy import func, exc

from application.db import db
from application.models import ExampleModel


class IntegrityErrorException(Exception):
    pass


class ExampleModelController:
    def __len__(self):
        return db.session.query(func.count(ExampleModel.id)).scalar()

    def add(self, name: str) -> None:
        example_model_object = ExampleModel(name)
        try:
            db.session.add(example_model_object)
            db.session.commit()
        except (exc.IntegrityError, sqlite3.IntegrityError):
            db.session.rollback()
            raise IntegrityErrorException

    def get(self, name: str) -> ExampleModel:
        return ExampleModel.query.filter_by(name=name).first()

    def edit(self, name: str, new_name: str) -> None:
        example_model_object = self.get(name)
        example_model_object.name = new_name
        db.session.commit()

    def get_all(self):
        return ExampleModel.query.all()

    def delete_all(self):
        ExampleModel.query.delete()
        db.session.commit()
