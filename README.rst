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

Features
--------

* Easily serve your single page javascript applications from Django.
* Optionally cache your templates for a configurable amount of time.
* Works with ember-cli-deploy and more specifically with `ember-cli-deploy-mysql <https://github.com/mwpastore/ember-cli-deploy-mysql>`_.

Deploying Your Single Page Application
---------------------------------------

You can publish a new template to your database in any way you choose. We assume that you will
use this to serve a Ember application, and the index template has been deployed
to the database. The easiest way to deploy it is to use
`ember-cli-deploy-mysql <https://github.com/mwpastore/ember-cli-deploy-mysql>`_.

If you are not using Ember you can still use this project to serve your application. You just
have to properly deploy your template to your MySQL database. For template model field reference
read the `docs <https://django-database-views.readthedocs.io>`_.

Running Tests
-------------

To run tests use the following commands::

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
