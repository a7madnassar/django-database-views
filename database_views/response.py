from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template.response import TemplateResponse
from django.template.base import Template


from .mixins import CachingMixin


class DatabaseTemplateResponse(TemplateResponse):
    CURRENT_KEY = 'current'
    model = None
    template_name = None
    content_type = 'text/html'
    cached = False

    @property
    def key(self):
        if self.template_name and ':' in self.template_name:
            return self.template_name.split(':')[1]

    def _get_pointer(self):
        """
        Get the current template key pointer object from the database.

        :return: DatabaseTemplate or None
        """
        return self.model.objects.get(key=self.CURRENT_KEY)

    def _get_object(self):
        """
        Get the template object from the database. Based on the key, this method will either get
        the template with the given key or the current template. Getting the current template
        requires looking up the current key pointer in the database first.

        :return: DatabaseTemplate or None
        """
        if self.model is None:
            raise ValueError('The `model` property must be a Django model class.')

        key = self.key
        if key == self.CURRENT_KEY:
            pointer = self._get_pointer()
            key = pointer.value

        criteria = {'key__startswith': key}

        return self.model.objects.get(**criteria)

    def _get_content(self):
        template = self._get_object()

        return template.value

    def resolve_template(self, template):
        """
        Resolve the template to be served. This will extract the template contents from the
        database and will return a Template object.

        :param template: Template names as a list
        :return: Template: The template object.
        """
        self.template_name = template[0]

        try:
            content = self._get_content()
        except ObjectDoesNotExist:
            raise Http404
        else:
            return Template(content)


class CachedTemplateResponse(DatabaseTemplateResponse, CachingMixin):

    cache_prefix = 'template'

    @property
    def cache_name(self):
        return self.template_name

    def _get_content(self):
        """
        Get the contents of the template from cache or from the database.

        :return: string or None: The contents of the target template
        """
        content = self._get_cache()
        if content is None:
            template =  self._get_object()
            content = template.value
            self._set_cache(content)

        return content
