=====
Usage
=====

Add `database_views` to your `INSTALLED_APPS`::

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
    from database_views.response import DatabaseTemplateResponse
    from myapp.models import IndexTemplate


    class IndexView(DatabaseTemplateView):
        model = IndexTemplate
        response_class = DatabaseTemplateResponse

It is recommended to cache template responses so the application doesn't query the database every
time the template is served. This package provides a class to handle response caching for a
configurable amount of time. To use the provided cached response, define your view as follows::

    from database_views.views import DatabaseTemplateView
    ffrom database_views.views import CachedTemplateResponse
    from myapp.models import IndexTemplate


    class IndexView(DatabaseTemplateView):
        model = IndexTemplate
        response_class = CachedTemplateResponse

To configure the cache TTL for the template response, set the `TEMPLATE_CACHE_TTL` constant in
your settings file. For example::

    TEMPLATE_CACHE_TTL = 24 * 60 * 60  # Cache template response for 24 hours.

Add a route for your index page view in your project's urls.py file::

    from myapp.views import IndexView

    urlpatterns = [
        ...
        url(r'^$', IndexView.as_view())
        ...
    ]

That's it!! Go to your new route and you should see your single page app's index template served.
Please ensure that you configure the serving of your app's static assets properly.
