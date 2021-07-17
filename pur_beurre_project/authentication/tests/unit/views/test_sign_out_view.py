# pylint: disable=C0116
"""Test sign out view module.
"""
from django.test import TestCase

from authentication.views.sign_out_view import SignOutView


class TestSignOutView(TestCase):
    """Test sign out view class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.sign_out_view = SignOutView()

    def test_init__with_sign_out_view(self):
        self.assertTrue(self.sign_out_view)

    def test_init_with_attr_data_redirect(self):
        self.assertEqual(
            self.sign_out_view._data['redirect'],
            'supersub:index'
        )
