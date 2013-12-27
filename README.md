Flask-Celery3
=============
Easily integrate Celery 3 in your Flask apps.

Introduction
------------
This flask extension makes it very easy for you to integrate Celery in your
flask apps. Previously there was the Flask-Celery extensions which worked for
Celery 2, but recently Celery updated to version 3, which neede a lot less
integration. Since then, the Flask docs showed an easy way to add Celery
functionality to your app. This method however needed you to add some
`make_celery` method to somewhere in your app, in every app.

This plugin takes the code the Flask docs give and makes it easy for you to
include it in your project.


Installation
------------
Just do

    pip install Flask-Celery3

Usage
-----
After installing, in your app:

    from flask import Flask
    from flask.ext.celery3 import make_celery
    app = Flask(__name__)
    celery = make_celery(app)

Make sure you have your broker up and running and correctly configured in your
flask config.


More info
---------
For more information on Flask and Celery, refer to the Flask docs at:
http://flask.pocoo.org/docs/patterns/celery/


License
-------
This plugin is MIT-licensed. See the LICENSE file.
