# pylint: disable=C0116
"""Test sign in view module.
"""
from django.test import TestCase

from authentication.views.sign_in_view import SignInView


class TestSignInView(TestCase):
    """Test sign in view class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.sign_in_view = SignInView()

    def test_init__with_sign_in_view(self):
        self.assertTrue(self.sign_in_view)

    def test_init_with_attr_data_render(self):
        self.assertEqual(
            self.sign_in_view.data['render'],
            'authentication/sign_in.html'
        )

    def test_init_with_attr_data_redirect(self):
        self.assertEqual(
            self.sign_in_view.data['redirect'],
            'supersub:index'
        )
