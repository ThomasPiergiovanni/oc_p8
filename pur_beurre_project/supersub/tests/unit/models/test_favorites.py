from django.db import models
from django.test import TestCase

from authentication.models import CustomUser
from authentication.tests.unit.models.test_custom_user import CustomUserTest
from supersub.models.favorites import Favorites
from supersub.models.product import Product
from supersub.tests.unit.models.test_category import CategoryTest
from supersub.tests.unit.models.test_product import ProductTest


class FavoritesTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        CategoryTest().emulate_category()
        ProductTest().emulate_product()
        CustomUserTest().emulate_custom_user()
        cls.emulate_favorites()
    
    @classmethod
    def emulate_favorites(cls):
        Favorites.objects.create(product_id=1, custom_user_id=1)

    def test_favorites_with_attr_product(self):
        favorites_field = Favorites._meta.get_field('product')
        self.assertTrue(favorites_field)
        self.assertEquals(
            type(favorites_field),
            type(models.ForeignKey(Product, models.CASCADE)))
    
    def test_favorites_with_attr_custom_user(self):
        favorites_field = Favorites._meta.get_field('custom_user')
        self.assertTrue(favorites_field)
        self.assertEquals(
            type(favorites_field),
            type(models.ForeignKey(CustomUser, models.CASCADE)))
    
    def test_favorites_with_instance(self):
        favorites = Favorites.objects.get(pk=1)
        self.assertIsInstance(favorites, Favorites)
        self.assertEquals(favorites.product_id, 1)
        self.assertEquals(favorites.custom_user_id, 1)

    def test__str__with_email(self):
        favorite = Favorites.objects.get(pk=1)
        self.assertEqual(favorite.__str__(), 'testuser@email.com')