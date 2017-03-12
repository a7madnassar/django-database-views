import mock
import pytest

from database_views.views import DatabaseTemplateView


class TestDatabaseTemplateView:

    @pytest.fixture
    def instance(self):
        return DatabaseTemplateView()

    def test_key_property_returns_key_from_query_string(self, instance):
        key = 'test'
        GET = {'key': key}
        request = mock.MagicMock(GET=GET)
        instance.request = request

        assert instance.key == key

    def test_key_property_returns_key_from_query_string(self, instance):
        GET = {}
        request = mock.MagicMock(GET=GET)
        instance.request = request

        assert instance.key == 'current'

    @mock.patch('database_views.views.DatabaseTemplateView.key', new_callable=mock.PropertyMock)
    def test_template_name_property_returns_expected_template_name(self, key, instance):
        key.return_value = 'test'

        instance.template_name == 'main:test'
