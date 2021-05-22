from django.db import models
from django.test import TestCase

from supersub.models.product import Product
from supersub.tests.unit.models.test_category import CategoryTest


class ProductTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        CategoryTest().emulate_category()
        cls.emulate_product()
    
    @classmethod
    def emulate_product(cls):
        Product.objects.create(
            id=1,
            id_origin = 'fevfvf',
            name = 'Product_for_test',
            nutriscore_grade = 'A',
            fat = 4.56,
            saturated_fat = 5.56,
            sugar=6.56,
            salt=7.56,
            image='www.imageurlbidon.com',
            url='www.urlbidon.com',
            categories='cat1, cat2, cat3',
            category_id=1
        )
        Product.objects.create(
            id=2,
            id_origin = 'kmihnl',
            name = 'Product_for_test2',
            nutriscore_grade = 'A',
            fat = 94.56,
            saturated_fat = 95.56,
            sugar=96.56,
            salt=97.56,
            image='www.imageurlbidon2.com',
            url='www.urlbidon.com',
            categories='cat1, cat2, cat3',
            category_id=1
        )
        Product.objects.create(
            id=3,
            id_origin = 'zeregrt',
            name = 'Product_for_test3',
            nutriscore_grade = 'A',
            fat = 94.56,
            saturated_fat = 95.56,
            sugar=96.56,
            salt=97.56,
            image='www.imageurlbidon3.com',
            url='www.urlbidon.com',
            categories='cat1, cat2, cat3',
            category_id=1
        )

    def test_product_with_product(self):
        product = Product.objects.get(pk=1)
        self.assertIsInstance(product, Product)
    
    def test_product_with_attrs_exist(self):
        self.assertTrue(Product._meta.get_field('name'))
        self.assertTrue(Product._meta.get_field('nutriscore_grade'))
        self.assertTrue(Product._meta.get_field('fat'))
        self.assertTrue(Product._meta.get_field('saturated_fat'))
        self.assertTrue(Product._meta.get_field('sugar'))
        self.assertTrue(Product._meta.get_field('salt'))
        self.assertTrue(Product._meta.get_field('image'))
        self.assertTrue(Product._meta.get_field('url'))
        self.assertTrue(Product._meta.get_field('categories'))
        self.assertTrue(Product._meta.get_field('category'))
    
    
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
    

    

    

    def test_product_with_attr_id(self):
        product = Product.objects.get(pk=1)
        self.assertEquals(product.id, 1)
    
    def test_product_with_attr_name(self):
        product = Product.objects.get(pk=1)
        self.assertEquals(product.name, "Product_for_test")
    
