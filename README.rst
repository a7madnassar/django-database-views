=====================
django-database-views
=====================

.. image:: https://badge.fury.io/py/django-database-views.svg
    :target: https://badge.fury.io/py/django-database-views

.. image:: https://travis-ci.org/a7madnassar/django-database-views.svg?branch=master
    :target: https://travis-ci.org/a7madnassar/django-database-views

.. image:: https://coveralls.io/repos/github/a7madnassar/django-database-views/badge.svg?branch=master
    :target: https://coveralls.io/github/a7madnassar/django-database-views?branch=master



Serve your single page Javascript applications from Django.

Documentation
-------------

The full documentation is at https://django-database-views.readthedocs.io.

Requirements
------------

* Django > 1.8
* A database engine such as MySQL

Quickstart
----------
Install django-database-views using pip::

    pip install django-database-views

Add it to your installed apps::

    INSTALLED_APPS = (
        ...
        'database_views.apps.DatabaseViewsConfig',
        ...
    )

Create a model to store versions for your index template in your app's models.py::

    from database_views.models import AbstractTemplate


    class IndexTemplate(AbstractTemplate):

        class Meta:
            db_table = 'your_table_name' # For example 'index_template'.

Create a class-based view for your single page app in your app's views.py and assign your model
to its `model` property::

    from database_views.views import DatabaseTemplateView
    from database_views.views import CachedTemplateResponse
    from myapp.models import IndexTemplate


    class IndexView(DatabaseTemplateView):
        app_name = 'main'
        model = IndexTemplate
        response_class = CachedTemplateResponse

Add a route for your index page view in your project's urls.py file::

    from myapp.views import IndexView

    urlpatterns = [
        ...
        url(r'^$', IndexView.as_view())
        ...
    ]

That's it!! Go to your new route and you should see your single page app's index template served.
Please ensure that you configure the serving of your app's static assets properly.

Features
--------

* Easily serve your single page javascript applications from Django.
* Optionally cache your templates for a configurable amount of time.
* Works with ember-cli-deploy and more specifically with `ember-cli-deploy-mysql <https://github.com/mwpastore/ember-cli-deploy-mysql>`_.

Running Tests
-------------

To run tests use the following commands from the root of this project::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ py.test

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
