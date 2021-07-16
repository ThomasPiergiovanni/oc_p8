# pylint: disable=C0116
"""Test account view module.
"""
from django.test import TestCase

from authentication.views.account_view import AccountView


class TestAccountView(TestCase):
    """Test account view class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.account_view = AccountView()

    def test_init__with_account_view(self):
        self.assertTrue(self.account_view)

    def test_init_with_attr_data_render(self):
        self.assertEqual(
            self.account_view._data['render'],
            'authentication/account.html'
        )

    def test_init_with_attr_data_redirect(self):
        self.assertEqual(
            self.account_view._data['redirect'],
            'authentication:sign_in'
        )
