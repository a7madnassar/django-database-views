# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from .response import DatabaseTemplateResponse, CachedTemplateResponse


class DatabaseTemplateView(TemplateView):
    """
    Base template view class.
    """

    app_name = None
    model = None

    def __init__(self):
        if self.response_class is not None and hasattr(self.response_class, 'model'):
            self.response_class.model = self.model

    @property
    def key(self):
        return self.request.GET.get('key', 'current')

    @property
    def template_name(self):
        return '{}:{}'.format(self.app_name, self.key)
