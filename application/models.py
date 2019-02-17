from application import db


class ExampleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return "<ExampleModel #{}, {}>".format(self.id, self.name)

    def __str__(self):
        return "#{}: {}".format(self.id, self.name)
