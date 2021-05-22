from django.test import TestCase

from supersub.models.product import Product


class ProductTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
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

    def test_category_with_attr_id_is_unique(self):
        category = Category.objects.get(pk=1)
        unique_field = category._meta.get_field('name').unique
        self.assertEquals(unique_field, True)
    
    def test_category_with_attr_name_max_lenght(self):
        category = Category.objects.get(pk=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)
    
    def test_category_with_attr_url_max_lenght(self):
        category = Category.objects.get(pk=1)
        max_length = category._meta.get_field('url').max_length
        self.assertEquals(max_length, 200)