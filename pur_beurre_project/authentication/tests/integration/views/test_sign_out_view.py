# pylint: disable=C0116
"""Test sign out view module.
"""
from django.test import TestCase


class SignOutViewTest(TestCase):
    """Test sign out view class.
    """
    def test_get_with_redirect(self):
        response = self.client.get('/authentication/sign_out/', follow=True)
        self.assertEqual(response.redirect_chain[0][0], '/supersub/')
