# pylint: disable=C0116
"""Test register favorite module.
"""
from django.test import TestCase

from supersub.views.register_favorite_view import RegisterFavoriteView


class TestRegisterFavoriteView(TestCase):
    """Test register favorite class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.register_favorite = RegisterFavoriteView()

    def test_init__with_register_favorite(self):
        self.assertTrue(self.register_favorite)

    def test_init_with_attr_data_render(self):
        self.assertEqual(
            self.register_favorite.data['redirect'],
            'supersub:product_detail'
        )
