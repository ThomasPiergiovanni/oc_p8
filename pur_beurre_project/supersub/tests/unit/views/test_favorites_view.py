from django.test import TestCase

from supersub.views.favorites_view import FavoritesView


class TestFavoritesView(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        cls.favorites_view = FavoritesView()

    def test___init__with_favorites(self):
        self.assertTrue(self.favorites_view)
    
    def test__init__with_attr_data_render(self):
        self.assertEqual(
            self.favorites_view.data['render'],
            'supersub/favorites.html')
    
    def test__init__with_attr_data_redirect(self):
        self.assertEqual(
            self.favorites_view.data['redirect'],
            'supersub:index' )