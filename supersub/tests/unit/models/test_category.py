# pylint: disable=C0116, E1101, W0212
"""Test category module.
"""
from django.db import models
from django.test import TestCase

from supersub.models.category import Category


class CategoryTest(TestCase):
    """Test category class.
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
        self.assertEqual(category.name, "CategorieOne")
        self.assertEqual(category.url, "www.categorie_test.com")

    def test_category_with_attr_name(self):
        category_field = Category._meta.get_field('name')
        self.assertTrue(category_field)
        self.assertEqual(type(category_field), type(models.CharField()))
        self.assertEqual(category_field.max_length, 200)
        self.assertEqual(category_field.unique, True)

    def test_category_with_attr_url(self):
        category_field = Category._meta.get_field('url')
        self.assertTrue(category_field)
        self.assertEqual(type(category_field), type(models.URLField()))
        self.assertEqual(category_field.max_length, 200)
