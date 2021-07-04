from django.test import TestCase

from authentication.tests.unit.models.test_custom_user import CustomUserTest
from supersub.models.favorites import Favorites
from supersub.tests.integration.models.test_category import CategoryTest
from supersub.tests.integration.models.test_product import ProductTest


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
    
    def test_favorites_with_instance(self):
        favorites = Favorites.objects.get(pk=1)
        self.assertIsInstance(favorites, Favorites)
        self.assertEquals(favorites.product_id, 1)
        self.assertEquals(favorites.custom_user_id, 1)

    def test__str__with_email(self):
        favorite = Favorites.objects.get(pk=1)
        self.assertEqual(favorite.__str__(), 'testuser@email.com')