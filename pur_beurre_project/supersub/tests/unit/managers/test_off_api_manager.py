from django.test import TestCase, RequestFactory
from unittest.mock import patch

from django.http import HttpResponse

from supersub.models.category import Category

from supersub.manager.off_api_manager import OffApiManager
from supersub.tests.unit.models.test_category import CategoryTest


class OffApiManagerTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        cls.emulate_categories_response()
        cls.emulate_products_response()
        cls.manager = OffApiManager()
        CategoryTest.emulate_category()
    
    @classmethod
    def emulate_categories_response(cls):
        cls.categories_response = {
            "count": 19982,
            "tags": [
                {
                    "id": "en:snacks",
                    "known": 1,
                    "name": "Snacks",
                    "products": 54568,
                    "url": "https://fr.openfoodfacts.org/categorie/snacks"
                },
                {
                    "id": "en:viennoiseries",
                    "known": 1,
                    "name": "Viennoiseries",
                    "products": 4498,
                    "url": "https://fr.openfoodfacts.org/categorie/viennoiseries"
                }
            ]
        }

    @classmethod
    def emulate_products_response(cls):
        cls.products_response = {
            "count": 54568,
            "page": 1,
            "page_count": 50,
            "page_size": 50,
            "products": [
                {
                    "categories": "Snacks,Snacks sucrés,Biscuits et gâteaux,Biscuits,Biscuits au chocolat",
                    "categories_hierarchy": [
                        "en:snacks",
                        "en:sweet-snacks",
                        "en:biscuits-and-cakes",
                        "en:biscuits",
                        "en:chocolate-biscuits"
                    ],
                    "id": "7622210449283",
                    "image_small_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.429.200.jpg",
                    "nutriments": {
                        "fat_100g": 17,
                        "salt_100g": 0.58,
                        "saturated-fat_100g": 5.6,
                        "sugars_100g": 32
                    },
                    "nutriscore_grade": "d",
                    "product_name": "Prince Chocolat",
                    "url": "https://fr.openfoodfacts.org/produit/7622210449283/prince-chocolat-lu",
                },
                ## That next produxt has no nutriscore key
                {
                    "categories": "Snacks,Snacks sucrés,Biscuits et gâteaux,Biscuits,Biscuits au chocolat",
                    "categories_hierarchy": [
                        "en:snacks",
                        "en:sweet-snacks",
                        "en:biscuits-and-cakes",
                        "en:biscuits",
                        "en:chocolate-biscuits"
                    ],
                    "id": "7622210449283",
                    "image_small_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.429.200.jpg",
                    "nutriments": {
                        "fat_100g": 17,
                        "salt_100g": 0.58,
                        "saturated-fat_100g": 5.6,
                        "sugars_100g": 32
                    },
                    "product_name": "Prince Chocolat Test 2",
                    "url": "https://fr.openfoodfacts.org/produit/7622210449283/prince-chocolat-lu",
                },
            ],
            "skip": 0
        }

    def mock_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.response = None

            def json(self):
                self.response = {"key1": "value1"}
                return self.response

        return MockResponse()

    @patch(
        'supersub.manager.off_api_manager.requests.get',
        side_effect=mock_requests_get)
    def test_download_catgories_with_mock(self, mock_get):
        manager = OffApiManager()
        manager.download_categories()
        self.assertEqual(manager.categories_response, {"key1": "value1"})

    def test_filter_categories_with_category(self):
        self.manager.categories_response = self.categories_response
        self.manager.filter_categories()
        self.assertEqual(self.manager.categories[0]['id'], "en:snacks")
    
    @patch(
        'supersub.manager.off_api_manager.requests.get',
        side_effect=mock_requests_get)
    def test_download_products_with_mock(self, mock_get):
        category = Category.objects.get(pk=1) 
        manager = OffApiManager()
        manager.download_products(category)
        self.assertEqual(manager.products_response, {"key1": "value1"})
    
    def test_filter_products_with_missing_keyword(self):
        self.manager.products_response = self.products_response
        self.manager.filter_products()
        missing_keyword = True
        try:
            if self.manager.products[1]:
                missing_keyword = False
        except:
            pass
        self.assertTrue(missing_keyword)
    
    def test_filter_products_with_product(self):
        self.manager.products_response = self.products_response
        self.manager.filter_products()
        self.assertEqual(
            self.manager.products[0]['product_name'],
            "Prince Chocolat")
