# pylint: disable=C0116, W0212
"""Test index view module.
"""
from django.test import TestCase

from supersub.views.index_view import IndexView


class TestIndexView(TestCase):
    """Test index view class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.index_view = IndexView()

    def test_init__with_index_view(self):
        self.assertTrue(self.index_view)

    def test_init_with_attr_data_render(self):
        self.assertEqual(
            self.index_view._data['render'],
            'supersub/index.html'
        )
