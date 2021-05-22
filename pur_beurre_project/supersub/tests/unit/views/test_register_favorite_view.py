from django.test import TestCase
from django.http import HttpResponseRedirect
from django.urls import reverse

from authentication.models import CustomUser
from authentication.tests.unit.models.test_custom_user import CustomUserTest
from supersub.models.favorites import Favorites
from supersub.tests.unit.models.test_category import CategoryTest
from supersub.tests.unit.models.test_product import ProductTest
from supersub.tests.unit.models.test_favorites import FavoritesTest


class RegisterFavoriteViewTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        CategoryTest().emulate_category()
        ProductTest().emulate_product()
        CustomUserTest().emulate_custom_user()
        FavoritesTest().emulate_favorites()
    
    def setUp(self):
        self.client.login(email='testuser@email.com', password='_Xxxxxxx')
        
    def test_get_with_status_code_200(self):
        self.response = self.client.get('/supersub/register_favorite/1', follow=True)
        self.assertEqual(self.response.status_code, 200)
    
    def test_get_with_message_warning(self):
        self.response = self.client.get('/supersub/register_favorite/1', follow=True)
        messages = self.response.context['messages']
        for message in messages:
            self.assertEqual(message.level_tag, 'warning')
            self.assertEqual(message.message, "Produit déja enregistré")
    
    def test_get_with_favorites_saved(self):
        self.response = self.client.get('/supersub/register_favorite/2', follow=True)
        new_favorite = Favorites.objects.get(
            product_id__exact=2,
            custom_user_id__exact=1)
        self.assertTrue(new_favorite)

    def test_get_with_message_success(self):
        self.response = self.client.get('/supersub/register_favorite/2', follow=True)
        messages = self.response.context['messages']
        for message in messages:
            self.assertEqual(message.level_tag, 'success')
            self.assertEqual(message.message, "Produit enregistré!")
    



