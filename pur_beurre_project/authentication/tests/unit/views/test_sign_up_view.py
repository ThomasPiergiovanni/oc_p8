# pylint: disable=C0116
"""Test sign up view module.
"""
from django.test import TestCase

from authentication.views.sign_up_view import SignUpView


class TestSignUpView(TestCase):
    """Test sign up view class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.sign_up_view = SignUpView()

    def test_init__with_sign_up_view(self):
        self.assertTrue(self.sign_up_view)

    def test_init_with_attr_data_render(self):
        self.assertEqual(
            self.sign_up_view.data['render'],
            'authentication/sign_up.html'
        )

    def test_init_with_attr_data_redirect(self):
        self.assertEqual(
            self.sign_up_view.data['redirect'],
            'authentication:sign_in'
        )
