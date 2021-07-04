from django.db import models
from django.test import TestCase

from supersub.models.category import Category


class CategoryTest(TestCase):
    """
    """  
    def test_category_with_attr_name(self):
        category_field = Category._meta.get_field('name')
        self.assertTrue(category_field)
        self.assertEquals(type(category_field), type(models.CharField()))
        self.assertEquals(category_field.max_length, 200)
        self.assertEquals(category_field.unique, True)
    
    def test_category_with_attr_url(self):
        category_field = Category._meta.get_field('url')
        self.assertTrue(category_field)
        self.assertEquals(type(category_field), type(models.URLField()))
        self.assertEquals(category_field.max_length, 200)

