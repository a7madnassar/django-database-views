# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


class DatabaseTemplateView(TemplateView):
    """
    Base template view class.
    """

    app_name = 'main'

    @property
    def key(self):
        return self.request.GET.get('key', 'current')

    @property
    def template_name(self):
        return '{}:{}'.format(self.app_name, self.key)
