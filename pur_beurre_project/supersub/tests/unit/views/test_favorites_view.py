# pylint: disable=C0116
"""Test Favorites view module.
"""
from django.test import TestCase

from authentication.tests.integration.models.test_custom_user import (
    CustomUserTest
)
from supersub.tests.unit.models.test_category import CategoryTest
from supersub.tests.unit.models.test_favorites import FavoritesTest
from supersub.tests.integration.models.test_product import ProductTest
from supersub.views.favorites_view import FavoritesView


class TestFavoritesView(TestCase):
    """Test Favorites view class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.favorites_view = FavoritesView()
        CategoryTest.emulate_category()
        ProductTest.emulate_product()
        CustomUserTest.emulate_custom_user()

    def test_init__with_favorites(self):
        self.assertTrue(self.favorites_view)

    def test_init_with_attr_data_render(self):
        self.assertEqual(
            self.favorites_view.data['render'],
            'supersub/favorites.html'
        )

    def test_init_with_attr_data_redirect(self):
        self.assertEqual(
            self.favorites_view.data['redirect'],
            'supersub:index'
        )

    def test_get_with_response_200_with_favs_and_logged_in(self):
        FavoritesTest.emulate_favorites()
        self.client.login(email='testuser@email.com', password='_Xxxxxxx')
        response = self.client.get('/supersub/favorites/')
        self.assertEqual(response.status_code, 200)

    def test_get_with_favorite(self):
        FavoritesTest.emulate_favorites()
        self.client.login(email='testuser@email.com', password='_Xxxxxxx')
        response = self.client.get('/supersub/favorites/')
        self.assertEqual(response.context['page_obj'][0].custom_user_id, 1)

    def test_get_with_message_warning(self):
        self.client.login(
            email='testuser@email.com',
            password='_Xxxxxxx'
        )
        response = self.client.get('/supersub/favorites/', follow=True)
        messages = response.context['messages']
        for message in messages:
            self.assertEqual(message.level_tag, 'warning')
            self.assertEqual(
                message.message,
                "Vous n'avez enregistré aucun favoris jusqu'à présent"
            )

    def test_get_with_message_error(self):
        response = self.client.get('/supersub/favorites/', follow=True)
        messages = response.context['messages']
        for message in messages:
            self.assertEqual(message.level_tag, 'error')
            self.assertEqual(
                message.message,
                "Connectez-vous pour consulter vos favoris!"
            )
