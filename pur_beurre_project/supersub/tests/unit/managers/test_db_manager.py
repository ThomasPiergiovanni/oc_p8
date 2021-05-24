from django.test import TestCase

from supersub.manager.db_manager import DbManager
from supersub.models.category import Category
from supersub.tests.unit.models.test_category import CategoryTest


class DbManagerTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        cls.db_manager = DbManager()
        cls.emulate_off_api_manager_categories = None

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
    
    def test_insert_categories_with_raw_categories(self):
        pass

    def emulate_off_api_manager_categories(self):
        pass
    

