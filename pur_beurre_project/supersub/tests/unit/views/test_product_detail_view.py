# pylint: disable=C0116
"""Test index view module.
"""
from django.test import TestCase

from supersub.views.product_detail_view import ProductDetailView


class TestProductDetailView(TestCase):
    """Test index view class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.product_detail_view = ProductDetailView()

    def test_init__with_product_detail_view(self):
        self.assertTrue(self.product_detail_view)

    def test_init_with_attr_data_render(self):
        self.assertEqual(
            self.product_detail_view.data['render'],
            'supersub/product_detail.html'
        )
