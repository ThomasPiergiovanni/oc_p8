from django.db import models
from django.test import TestCase

from authentication.models import CustomUser
from supersub.models.favorites import Favorites
from supersub.models.product import Product


class FavoritesTest(TestCase):
    """
    """
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
