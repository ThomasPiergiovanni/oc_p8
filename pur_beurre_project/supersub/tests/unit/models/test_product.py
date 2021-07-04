from django.db import models
from django.test import TestCase

from supersub.models.category import Category
from supersub.models.product import Product


class ProductTest(TestCase):
    """
    """
    def test_product_with_attr_id_origin(self):
        product_field = Product._meta.get_field('id_origin')
        self.assertTrue(product_field)
        self.assertEquals(type(product_field), type(models.CharField()))
        self.assertEquals(product_field.max_length, 200)
 
    def test_product_with_attr_name(self):
        product_field = Product._meta.get_field('name')
        self.assertTrue(product_field)
        self.assertEquals(type(product_field), type(models.CharField()))
        self.assertEquals(product_field.max_length, 200)
        self.assertEquals(product_field.unique, True)

    def test_product_with_attr_nutriscore_grade(self):
        product_field = Product._meta.get_field('nutriscore_grade')
        self.assertTrue(product_field)
        self.assertEquals(type(product_field), type(models.CharField()))
        self.assertEquals(product_field.max_length, 8)
    
    def test_product_with_attr_fat(self):
        product_field = Product._meta.get_field('fat')
        self.assertTrue(product_field)
        self.assertEquals(type(product_field), type(models.DecimalField()))
        self.assertEquals(product_field.max_digits, 8)
        self.assertEquals(product_field.decimal_places, 3)
    
    def test_product_with_attr_saturated_fat(self):
        product_field = Product._meta.get_field('saturated_fat')
        self.assertTrue(product_field)
        self.assertEquals(type(product_field), type(models.DecimalField()))
        self.assertEquals(product_field.max_digits, 8)
        self.assertEquals(product_field.decimal_places, 3)
    
    def test_product_with_attr_sugar(self):
        product_field = Product._meta.get_field('sugar')
        self.assertTrue(product_field)
        self.assertEquals(type(product_field), type(models.DecimalField()))
        self.assertEquals(product_field.max_digits, 8)
        self.assertEquals(product_field.decimal_places, 3)
    
    def test_product_with_attr_salt(self):
        product_field = Product._meta.get_field('sugar')
        self.assertTrue(product_field)
        self.assertEquals(type(product_field), type(models.DecimalField()))
        self.assertEquals(product_field.max_digits, 8)
        self.assertEquals(product_field.decimal_places, 3)
    
    def test_product_with_attr_image(self):
        product_field = Product._meta.get_field('image')
        self.assertTrue(product_field)
        self.assertEquals(type(product_field), type(models.URLField()))
        self.assertEquals(product_field.max_length, 200)

    def test_product_with_attr_url(self):
        product_field = Product._meta.get_field('url')
        self.assertTrue(product_field)
        self.assertEquals(type(product_field), type(models.URLField()))
        self.assertEquals(product_field.max_length, 200)

    def test_product_with_attr_categories(self):
        product_field = Product._meta.get_field('categories')
        self.assertTrue(product_field)
        self.assertEquals(type(product_field), type(models.TextField()))

    def test_product_with_attr_category(self):
        product_field = Product._meta.get_field('category')
        self.assertTrue(product_field)
        self.assertEquals(
            type(product_field),
            type(models.ForeignKey(Category, models.CASCADE)))
