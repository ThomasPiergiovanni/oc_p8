# pylint: disable=C0116
"""Test Favorites view module.
"""
from django.test import TestCase

from supersub.views.favorites_view import FavoritesView


class TestFavoritesView(TestCase):
    """Test Favorites view class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.favorites_view = FavoritesView()

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
