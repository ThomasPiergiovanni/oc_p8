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
    
    def test_product_with_attr_id_origin_exist(self):
        self.assertTrue(Product._meta.get_field('id_origin'))
    
    def test_product_with_attr_id_origin_type(self):
        field = Product._meta.get_field('id_origin')
        self.assertEquals(type(field), type(models.CharField()))
    
    def test_product_with_attr_id_origin_max_lenght(self):
        product = Product.objects.get(pk=1)
        field_max_length = product._meta.get_field('id_origin').max_length
        self.assertEquals(field_max_length, 200)
    
    def test_product_with_attr_name_is_unique(self):
        product = Product.objects.get(pk=1)
        field_unique = product._meta.get_field('name').unique
        self.assertEquals(field_unique, True)
    
    def test_product_with_attr_name_max_lenght(self):
        product = Product.objects.get(pk=1)
        field_max_length = product._meta.get_field('name').max_length
        self.assertEquals(field_max_length, 200)

    def test_product_with_attr_nutriscore_grade_max_lenght(self):
        product = Product.objects.get(pk=1)
        field_max_length = product._meta.get_field('nutriscore_grade').max_length
        self.assertEquals(field_max_length, 8)
    
    def test_product_with_attr_fat_max_digit(self):
        product = Product.objects.get(pk=1)
        field_max_digit = product._meta.get_field('fat').max_digits
        self.assertEquals(field_max_digit, 8)
    
    def test_product_with_attr_fat_decimal_place(self):
        product = Product.objects.get(pk=1)
        field_decimal_places = product._meta.get_field('fat').decimal_places
        self.assertEquals(field_decimal_places, 3)
    

    def test_product_with_attr_id(self):
        product = Product.objects.get(pk=1)
        self.assertEquals(product.id, 1)
    
    def test_product_with_attr_name(self):
        product = Product.objects.get(pk=1)
        self.assertEquals(product.name, "Product_for_test")
    
