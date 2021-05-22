from django.db import models
from django.test import TestCase

from supersub.models.category import Category
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
            fat = 4.561,
            saturated_fat = 5.561,
            sugar= 6.561,
            salt= 7.561,
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
            fat = 94.561,
            saturated_fat = 95.561,
            sugar= 96.561,
            salt= 97.561,
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
            fat = 94.561,
            saturated_fat = 95.561,
            sugar= 96.561,
            salt= 97.561,
            image='www.imageurlbidon3.com',
            url='www.urlbidon.com',
            categories='cat1, cat2, cat3',
            category_id=1
        )

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

    def test_product_with_product_instance(self):
        product = Product.objects.get(pk=1)
        self.assertIsInstance(product, Product)  

    def test_product_with_instance_id(self):
        product = Product.objects.get(pk=1)
        self.assertEquals(product.id, 1)

    def test_product_with_instance_id_origin(self):
        product = Product.objects.get(pk=1)
        self.assertEquals(product.id_origin, "fevfvf")

    def test_product_with_instance_name(self):
        product = Product.objects.get(pk=1)
        self.assertEquals(product.name, "Product_for_test")
    
    def test_product_with_instance_nutriscore_grade(self):
        product = Product.objects.get(pk=1)
        self.assertEquals(product.nutriscore_grade, "A")

    def test_product_with_instance_fat(self):
        product = Product.objects.get(pk=1)
        self.assertEquals(float(product.fat), 4.561)

    def test_product_with_instance_saturated_fat(self):
        product = Product.objects.get(pk=1)
        self.assertEquals(float(product.saturated_fat), 5.561)

    def test_product_with_instance_sugar(self):
        product = Product.objects.get(pk=1)
        self.assertEquals(float(product.sugar), 6.561)

    def test_product_with_instance_salt(self):
        product = Product.objects.get(pk=1)
        self.assertEquals(float(product.salt), 7.561)

    def test_product_with_instance_image(self):
        product = Product.objects.get(pk=1)
        self.assertEquals(product.image, "www.imageurlbidon.com")
    
    def test_product_with_instance_url(self):
        product = Product.objects.get(pk=1)
        self.assertEquals(product.url, "www.urlbidon.com")
    
    def test_product_with_instance_categories(self):
        product = Product.objects.get(pk=1)
        self.assertEquals(product.categories, "cat1, cat2, cat3")
    
    def test_product_with_instance_category(self):
        product = Product.objects.get(pk=1)
        self.assertEquals(product.category.id, 1)
    
