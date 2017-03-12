import mock
import pytest

from database_views.mixins import CachingMixin


class TestCachingMixin:

    @pytest.fixture
    def instance(self):
        instance = CachingMixin()
        instance.cache_name = 'main:current'
        instance.cache_prefix = 'template'

        return instance

    @pytest.fixture
    def key(self):
        return 'template:main:current'

    def test_key_property_returns_expected_value(self, key, instance):
        assert instance.key == key

    @mock.patch('database_views.mixins.cache.get')
    def test_get_cache_calls_cache_manager_get(self, get, key, instance):
        value = 'test'
        get.return_value = value

        result = instance._get_cache()

        get.assert_called_once_with(key)

        assert result == value

    @mock.patch('database_views.mixins.cache.set')
    def test_set_cache_calls_cache_manager_set_with_default(self, set, key, instance):
        value = 'test'
        instance._set_cache(value)

        set.assert_called_once_with(key, value, CachingMixin.DEFAULT_TTL)

    @mock.patch('database_views.mixins.settings')
    @mock.patch('database_views.mixins.cache.set')
    def test_set_cache_calls_cache_manager_set_with_settings_ttl(self, set, settings, key,
                                                                 instance):
        ttl = 1000
        settings.TEMPLATE_CACHE_TTL = ttl
        value = 'test'
        instance._set_cache(value)

        set.assert_called_once_with(key, value, ttl)

    @mock.patch('database_views.mixins.cache.delete')
    def test_delete_cache_calls_cache_manager_delete(self, delete, key, instance):
        instance._delete_cache()

        delete.assert_called_once_with(key)
