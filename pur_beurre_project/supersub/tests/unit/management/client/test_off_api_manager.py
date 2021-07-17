# pylint: disable=C0116, R0903, E1101, E0211, W0613
"""Test OFF API manager module.
"""
from unittest.mock import patch
from django.test import TestCase

from config.custom_settings.tests_variables import (
    OFF_API_CATEGORIES_W_KEYS,
    OFF_API_CATEGORIES_WO_KEYS,
    OFF_API_PRODUCTS
)
from supersub.models.category import Category
from supersub.management.client.off_api_manager import OffApiManager
from supersub.tests.unit.models.test_category import CategoryTest


class OffApiManagerTest(TestCase):
    """Test OFF API manager class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.emulate_categories_response()
        cls.emulate_keyrror_categories_response()
        cls.emulate_products_response()
        CategoryTest.emulate_category()

    def setUp(self):
        self.manager = OffApiManager()

    @classmethod
    def emulate_categories_response(cls):
        cls.categories_response = OFF_API_CATEGORIES_W_KEYS

    @classmethod
    def emulate_keyrror_categories_response(cls):
        cls.keyrror_categories_response = OFF_API_CATEGORIES_WO_KEYS

    @classmethod
    def emulate_products_response(cls):
        cls.products_response = OFF_API_PRODUCTS

    def mock_requests_get(*args, **kwargs):
        class MockResponse:
            """Class mocks a OFF API response
            """
            def __init__(self):
                self.response = None

            def json(self):
                self.response = {"key1": "value1"}
                return self.response

        return MockResponse()

    @patch(
        'supersub.management.client.off_api_manager.requests.get',
        side_effect=mock_requests_get)
    def test_download_catgories_with_mock(self, mock_get):
        manager = OffApiManager()
        manager.download_categories()
        self.assertEqual(manager.categories_response, {"key1": "value1"})

    def test_filter_categories_with_category(self):
        self.manager.categories_response = self.categories_response
        self.manager.filter_categories()
        self.assertEqual(self.manager.categories[0]['id'], "en:snacks")

    def test_filter_categories_with_keyerror(self):
        self.manager.categories_response = self.keyrror_categories_response
        self.manager.filter_categories()
        missing_key = True
        try:
            if self.manager.categories[0]['id']:
                missing_key = False
        except (KeyError, IndexError):
            pass
        self.assertTrue(missing_key)

    @patch(
        'supersub.management.client.off_api_manager.requests.get',
        side_effect=mock_requests_get)
    def test_download_products_with_mock(self, mock_get):
        category = Category.objects.get(pk=1)
        manager = OffApiManager()
        manager.download_products(category)
        self.assertEqual(manager.products_response, {"key1": "value1"})

    def test_filter_products_with_missing_keyword(self):
        self.manager.products_response = self.products_response
        self.manager.filter_products()
        missing_key = True
        try:
            if self.manager.products[1]:
                missing_key = False
        except (KeyError, IndexError):
            pass
        self.assertTrue(missing_key)

    def test_filter_products_with_product(self):
        self.manager.products_response = self.products_response
        self.manager.filter_products()
        self.assertEqual(
            self.manager.products[0]['product_name'],
            "Prince Chocolat"
        )
