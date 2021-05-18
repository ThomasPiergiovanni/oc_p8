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