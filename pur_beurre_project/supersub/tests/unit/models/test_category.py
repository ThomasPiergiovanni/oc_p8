from django.test import TestCase

from supersub.models.category import Category


class CategoryTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        cls.emulate_category()
    
    @classmethod
    def emulate_category(cls):
        Category.objects.create(
            id=1,
            name="CategorieOne",
            url="www.categorie_test.com")
    
    def test_category_with_category(self):
        category = Category.objects.get(pk=1)
        self.assertIsInstance(category, Category)
    
    def test_category_with_attr_id(self):
        category = Category.objects.get(pk=1)
        self.assertEqual(category.id, 1)
    
    def test_category_with_attr_name(self):
        category = Category.objects.get(pk=1)
        self.assertEqual(category.name, "CategorieOne")
    
    def test_category_with_attr_url(self):
        category = Category.objects.get(pk=1)
        self.assertEqual(category.url, "www.categorie_test.com")
