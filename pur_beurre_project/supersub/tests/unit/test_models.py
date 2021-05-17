from django.test import TestCase

# from supersub.models import Category, Product, Favorites

from supersub.models.category import Category
from supersub.models.product import Product
from supersub.models.favorites import Favorites


class ModelsTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(
            name="CategorieOne",
            url="www.categorie_test.com")
    
    def test_category_name_attribute_max_lenght(self):
        category = Category.objects.get(pk=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)
    
    def test_category_name_attribute_is_unique(self):
        category = Category.objects.get(pk=1)
        unique = category._meta.get_field('name').unique
        self.assertEquals(unique, True)

    def test_category_url_attribute_max_lenght(self):
        category = Category.objects.get(pk=1)
        max_length = category._meta.get_field('url').max_length
        self.assertEquals(max_length, 200)


