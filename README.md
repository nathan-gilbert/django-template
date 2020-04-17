# django-template

Simple base project for Django REST backend server.

Working through the tutorial here: <https://docs.djangoproject.com/en/3.0/intro/tutorial01/>

This is another tutorial for REST API + React: <https://www.valentinog.com/blog/drf/>

## Usage

* `coverage run --source='.' manage.py test`
* `coverage html`
* `coverage report`

Database setup:

* `python manage.py makemigrations quotes` -- create a migration
* `python manage.py migrate` - run the migration
* `python manage.py flush` - reset the database
* Delete the sqlite file and migrations to completely start over

## TODO

* Create simple frontend react SPA
* JWT