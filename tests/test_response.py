import mock
import pytest

from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template.base import Template

from database_views.response import DatabaseTemplateResponse, CachedTemplateResponse


def get_model_mock(return_value=None, side_effect=None):
    if return_value is None:
        obj = mock.Mock()
    else:
        obj = return_value

    if side_effect is None:
        kwargs = {'return_value': obj}
    else:
        kwargs = {'side_effect': side_effect}

    get = mock.MagicMock(**kwargs)
    objects = mock.MagicMock(get=get)
    model = mock.MagicMock(objects=objects)

    return model


class TestDatabaseTemplateResponse:

    @pytest.fixture
    def instance(self):
        instance = DatabaseTemplateResponse(None, None, None)

        return instance

    @pytest.fixture
    def template_names(self):
        return ['main:current']

    def test_key_property_returns_none_if_template_name_is_invalid(self, instance):
        template_name = 'main'
        instance.template_name = template_name

        assert instance.key is None

    def test_key_property_returns_expected_value(self, instance):
        template_name = 'main:current'
        instance.template_name = template_name

        assert instance.key == template_name.split(':')[1]

    def test_it_raises_value_error_if_model_is_none(self, template_names, instance):
        with pytest.raises(ValueError):
            instance.resolve_template(template_names)

    def test_it_raises_http404_if_no_template_found(self, instance):
        template_names = ['main:test']
        exception = ObjectDoesNotExist()
        model = get_model_mock(side_effect=exception)
        instance.model = model

        with pytest.raises(Http404):
            instance.resolve_template(template_names)

    @mock.patch('database_views.response.DatabaseTemplateResponse.key',
                new_callable=mock.PropertyMock)
    def test_it_raises_http404_if_no_pointer_found(self, key, template_names, instance):
        key.return_value = 'current'
        exception = ObjectDoesNotExist()
        model = get_model_mock(side_effect=exception)
        instance.model = model

        with pytest.raises(Http404):
            instance.resolve_template(template_names)

    @mock.patch('database_views.response.DatabaseTemplateResponse.key',
                new_callable=mock.PropertyMock)
    def test_it_resolves_current_template(self, key, template_names, instance):
        key.return_value = 'current'
        value = 'test'
        pointer = mock.MagicMock(value=value)
        template = mock.MagicMock(value=value)
        model = get_model_mock(side_effect=[pointer, template])
        instance.model = model

        result = instance.resolve_template(template_names)

        assert isinstance(result, Template)
        assert result.source == value

    @mock.patch('database_views.response.DatabaseTemplateResponse.key',
                new_callable=mock.PropertyMock)
    def test_it_resolves_template_with_key(self, key, template_names, instance):
        key.return_value = 'test'
        value = 'test'
        template = mock.MagicMock(value=value)
        model = get_model_mock(return_value=template)
        instance.model = model

        result = instance.resolve_template(template_names)

        assert isinstance(result, Template)
        assert result.source == value


class TestCachedTemplateResponse:

    @pytest.fixture
    def instance(self):
        return CachedTemplateResponse(None, None, None)

    @pytest.fixture
    def template_names(self):
        return ['main:current']

    def test_cache_name_property_returns_expected_value(self, instance):
        template_name = 'test'
        instance.template_name = template_name

        assert instance.cache_name == template_name

    @mock.patch.object(CachedTemplateResponse, '_get_cache')
    def test_it_will_raise_http404_if_no_content(self, get_cache, template_names, instance):
        get_cache.return_value = None

        exception = ObjectDoesNotExist()
        model = get_model_mock(side_effect=exception)
        instance.model = model

        with pytest.raises(Http404):
            instance.resolve_template(template_names)

    @mock.patch.object(CachedTemplateResponse, '_get_cache')
    def test_it_returns_cached_content(self, get_cache, template_names, instance):
        cache = 'test'
        get_cache.return_value = cache

        result = instance.resolve_template(template_names)

        assert get_cache.called
        assert result.source == cache

    @mock.patch.object(CachedTemplateResponse, '_set_cache')
    @mock.patch.object(CachedTemplateResponse, '_get_cache')
    def test_it_caches_and_returns_database_content(self, get_cache, set_cache, template_names,
                                                    instance):
        get_cache.return_value = None
        content = 'test'

        template = mock.Mock(value=content)
        model = get_model_mock(return_value=template)
        instance.model = model

        result = instance.resolve_template(template_names)

        set_cache.assert_called_once_with(content)

        assert result.source == content
