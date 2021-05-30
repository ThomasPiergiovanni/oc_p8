from django.test import TestCase

from supersub.manager.db_manager import DbManager
from supersub.models.category import Category
from supersub.models.product import Product
from supersub.tests.unit.models.test_category import CategoryTest
from supersub.tests.unit.models.test_product import ProductTest


class DbManagerTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        cls.emulate_off_api_manager_categories()
        cls.emulate_off_api_manager_products()
        cls.db_manager = DbManager()

    
    @classmethod
    def emulate_off_api_manager_categories(cls):
        cls.categories = [
            {
                'id': 'en:snacks',
                'known': 1,
                'name': 'Snacks',
                'products': 54568,
                'url': 'https://fr.openfoodfacts.org/categorie/snacks'
            },
            {
                "id": "en:breakfast-cereals",
                "known": 1,
                "name": "Céréales pour petit-déjeuner",
                "products": 4602,
                "url": "https://fr.openfoodfacts.org/categorie/cereales-pour-petit-dejeuner"
            }
        ]

    @classmethod
    def emulate_off_api_manager_products(cls):
        """Emulation of off api manager products attribute. It consist of 
        valid products that have been filtered out from api response to ensure
        it suits db requirements
        """
        cls.products = [
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
                {
                    "categories": "Snacks,Snacks sucrés,Biscuits et gâteaux,Biscuits,Biscuits au chocolat",
                    "categories_hierarchy": [
                        "en:snacks",
                        "en:sweet-snacks",
                        "en:biscuits-and-cakes",
                        "en:biscuits",
                        "en:chocolate-biscuits"
                    ],
                    "id": "7622210449283_dummy",
                    "image_small_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.429.200.jpg",
                    "nutriments": {
                        "fat_100g": 17,
                        "salt_100g": 0.58,
                        "saturated-fat_100g": 5.6,
                        "sugars_100g": 32
                    },
                    "nutriscore_grade": "d",
                    "product_name": "Prince Chocolat 2",
                    "url": "https://fr.openfoodfacts.org/produit/7622210449283/prince-chocolat-lu",
                },
        ]
    

    def test_drop_categories_with_categories(self):
        CategoryTest.emulate_category()
        self.db_manager.drop_categories()
        categories = Category.objects.all()
        for category in categories:
            self.assertIsNone(category)
    
    def test_get_categories_with_categories(self):
        CategoryTest.emulate_category()
        self.db_manager.get_categories()
        self.assertEquals(
            self.db_manager.categories_in_db[0].name,
            "CategorieOne")
    
    def test_insert_categories_with_category(self):
        self.db_manager.off_api_manager.categories = self.categories
        self.db_manager.insert_categories()
        category = Category.objects.get(pk=1)
        self.assertEquals(category.name, "Snacks")

    def test_drop_products_with_products(self):
        ProductTest.emulate_product()
        self.db_manager.drop_products()
        products = Product.objects.all()
        for product in products:
            self.assertIsNone(product)
    
    def test_insert_products_with_product(self):
        CategoryTest.emulate_category()
        self.db_manager.categories_in_db = Category.objects.all()
        self.db_manager.off_api_manager.products = self.products
        self.db_manager.insert_products()
        product = Product.objects.get(pk=1)
        product_2 = Product.objects.get(pk=2)
        self.assertEqual(product.name, "Prince Chocolat")
        self.assertEqual(product_2.name, "Prince Chocolat 2")
    

