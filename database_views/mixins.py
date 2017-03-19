from django.conf import settings
from django.core.cache import cache


class CachingMixin(object):
    """
    A mixin for cache management.
    """
    DEFAULT_TTL = 7 * 24 * 60 * 60  # 1 week.
    cache_prefix = ''
    cache_name = ''

    @property
    def key(self):
        return '{}:{}'.format(self.cache_prefix, self.cache_name)

    def _get_cache(self):
        return cache.get(self.key)

    def _set_cache(self, content):
        ttl = self.DEFAULT_TTL
        if hasattr(settings, 'TEMPLATE_CACHE_TTL'):
            ttl = settings.TEMPLATE_CACHE_TTL

        cache.set(self.key, content, ttl)

    def _delete_cache(self):
        cache.delete(self.key)
