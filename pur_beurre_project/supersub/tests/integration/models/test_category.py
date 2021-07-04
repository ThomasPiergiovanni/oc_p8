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
        self.assertEquals(category.name, "CategorieOne")
        self.assertEquals(category.url, "www.categorie_test.com")