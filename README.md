# Flask boilerplate

Simple example on how to configure Flask with SQLAlchemy (Dockerized).

## Running application:
```bash
docker-compose up
``` 

The page should be available under http://localhost:8000/

## Code

The initialisation of the application is written in `application/__init__.py`.

Setup is made in `run.py` using `FlaskConfig` object. 
The example also covers a usage of environmental variables (defined in `docker-compose.yml`).

## Tests

Example of tests configuration can be found in `tests/` directory.

To run tests, execute:
```bash
docker exec -it flask_app python -m unittest
```
 
## About the page
The main page http://localhost:8000 allows to see the content of a column in the database created by `models.py` `ExampleModel`.

### Add a new entry
Go to: http://localhost:8000/add?name=new_object_name to create a new entry. It should be now visible on the main page.

### Delete all entries
Go to: http://localhost:8000/delete_all to delete all `ExampleModel` entries.


