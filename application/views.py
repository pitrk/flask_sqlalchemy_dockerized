from flask import request, Blueprint
from flask_api import status

from application.model_controllers import ExampleModelController, IntegrityErrorException

router = Blueprint('router', __name__)

controller = ExampleModelController()


@router.route('/', methods=['GET'])
def index():
    objects_str = '<h1>Hello World</h1>'
    objects = controller.get_all()
    if len(objects) == 0:
        objects_str += "<p>No objects in the database! Use /add?name=object_name to add a new object.</p>"
    else:
        objects_str += '<ul>'
        for each in objects:
            objects_str += '<li>' + str(each) + '</li>'
        objects_str += '</ul>'
    return objects_str, status.HTTP_200_OK


@router.route('/add')
def add():
    name = request.args.get('name')
    if name is None:
        return "Bad request!", status.HTTP_400_BAD_REQUEST
    try:
        controller.add(name)
    except IntegrityErrorException:
        return "Object already exists!", status.HTTP_400_BAD_REQUEST
    return "OK", status.HTTP_201_CREATED


@router.route('/delete_all')
def delete_all():
    controller.delete_all()
    return "All objects removed!", status.HTTP_204_NO_CONTENT
