=====
Usage
=====

To use Django Database Views in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_database_views.apps.DatabaseViewsConfig',
        ...
    )

Add Django Database Views's URL patterns:

.. code-block:: python

    from django_database_views import urls as django_database_views_urls


    urlpatterns = [
        ...
        url(r'^', include(django_database_views_urls)),
        ...
    ]
