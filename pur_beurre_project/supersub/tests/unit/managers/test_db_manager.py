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
