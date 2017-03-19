=====
Usage
=====

Deploying Your Single Page Application
--------------------------------------

You can publish a new template to your database in any way you choose. We assume that you will
use this to serve an Ember application, and the index template has been deployed
to the database. The easiest way to deploy it is to use
`ember-cli-deploy-mysql <https://github.com/mwpastore/ember-cli-deploy-mysql>`_.

If you are not using Ember you can still use this project to serve your application. You just
have to properly deploy your template to your MySQL database and set it as the current one. For
more details about the template model schema. see the `Usage <https://django-database-views.readthedocs.io/en/latest/usage.html>`_
section.

Models
------

**AbstractTemplate**

The *AbstractTemplate* model represents a single template stored in the database. This model
creates a table in the database to hold all template-related information. This model has the
following fields defined:
    * key: A unique identifier for the template.
    * value: The template content.
    * created_at: Creation date and time.
    * gitsha: Reserved for future use.
    * deployer: Reserved for future use.

This schema is based on the implementation of the `django-cli-deploy-mysql <https://github
.com/mwpastore/ember-cli-deploy-mysql>`_ package. According to the deploy strategy implemented by
that package, a template version is activated by creating a record with the key `current` and the
key of the current version as its value. So for the current template to work properly your table
has to have two records in it. One for the template itself and another one for the current vesion
pointer.

**AbstractApplicationTemplate**

By default, this package is implemented to be compatible with Ember CLI deploy tools. However,
you can still use this package to implement a custom solution or change the way it works by default.

This model allows you to implement a model to store template for multiple applications.
This model extends the *AbstractTemplate* model and adds the following fields to it:
    * app_name: The name of the application that owns this template.
    * current: A boolean flag for the current version.

Cache Time to Live (TTL) Configuration
--------------------------------------
By default, if the *CachedTemplateResponse* class is used it will cache the contents of the
template for a week. To configure a different cache TTL for the template response, set the
*TEMPLATE_CACHE_TTL* setting in your settings module. For example::

    TEMPLATE_CACHE_TTL = 24 * 60 * 60  # Cache template response for 24 hours.

Disabling Cache
---------------
It is recommended to cache template responses so the application doesn't query the database every
time the template is served. If for any reason you need to disable the caching feature of the
template use the *DatabaseTemplateResponse* class instead as follows::

    from database_views.views import DatabaseTemplateView
    from database_views.response import DatabaseTemplateResponse
    from myapp.models import IndexTemplate


    class IndexView(DatabaseTemplateView):
        model = IndexTemplate
        response_class = DatabaseTemplateResponse
