from django.contrib import messages
from django.test import TestCase, RequestFactory
from django.contrib.auth import authenticate, login, logout

from authentication.models import CustomUser
from supersub.models.favorites import Favorites
from supersub.views.favorites_view import FavoritesView
from supersub.tests.unit.models.test_category import CategoryTest
from supersub.tests.unit.models.test_product import ProductTest


class TestFavoritesView(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        cls.favorites_view = FavoritesView()
        CategoryTest.emulate_category()
        ProductTest.emulate_product()
        cls.emulate_custom_user()
        cls.custom_user = CustomUser.objects.get(pk=1)
    
    @classmethod
    def emulate_custom_user(cls):
        CustomUser.objects.create_user(
                id=1,
                email='testuser@email.com',
                password='_Xxxxxxx',
                first_name='tester')
    
    def emulate_favorites(self):
        Favorites.objects.create(product_id=1, custom_user_id=1)

    def test___init__with_favorites(self):
        self.assertTrue(self.favorites_view)
    
    def test__init__with_attr_data_render(self):
        self.assertEqual(
            self.favorites_view.data['render'],
            'supersub/favorites.html')
    
    def test__init__with_attr_data_redirect(self):
        self.assertEqual(
            self.favorites_view.data['redirect'],
            'supersub:index')
    
    def test_get_with_response_200_with_favs_and_logged_in(self):
        self.emulate_favorites()
        self.client.login(email='testuser@email.com', password='_Xxxxxxx')
        response = self.client.get('/supersub/favorites/')
        self.assertEqual(response.status_code, 200)
    
    def test_get_with_favorite(self):
        self.emulate_favorites()
        self.client.login(email='testuser@email.com', password='_Xxxxxxx')
        response = self.client.get('/supersub/favorites/')
        self.assertEqual(response.context['page_obj'][0].custom_user_id, 1)
    
    def test_get_with_message_warning(self):
        self.client.login(
            email='testuser@email.com',
            password='_Xxxxxxx')
        response = self.client.get('/supersub/favorites/', follow=True)
        messages = response.context['messages']
        for message in messages:
            self.assertEqual(message.level_tag, 'warning')
            self.assertEqual(message.message, "Vous n'avez enregistré aucun"\
            " favoris jusqu'à présent")

    def test_get_with_message_error(self):
        response = self.client.get('/supersub/favorites/', follow=True)
        messages = response.context['messages']
        for message in messages:
            self.assertEqual(message.level_tag, 'error')
            self.assertEqual(message.message, "Connectez-vous pour"\
            " consulter vos favoris!")
