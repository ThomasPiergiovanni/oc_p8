from django.test import TestCase

from supersub.models.favorites import Favorites


class FavoritesTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        cls.emulate_favorites()
    
    @classmethod
    def emulate_favorites(cls):
        Favorites.objects.create(product_id=1, custom_user_id=1)