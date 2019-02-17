import os

from application import create_app


class FlaskConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


if os.environ['FLASK_ENV'] == 'development':
    debug = True
else:
    debug = False

create_app(FlaskConfig).run(debug=debug, host='0.0.0.0', port=int(os.environ['FLASK_PORT']))
