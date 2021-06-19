from django.test import TestCase

from authentication.managers.authentication_manager import AuthenticationManager
from authentication.tests.unit.models.test_custom_user import CustomUserTest


class AuthenticationManagerTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        CustomUserTest.emulate_custom_user()
    
    def setUp(self):
        self.client.login(
            email='testuser@email.com',
            password='_Xxxxxxx'
        )

    def test_logout_with_client_logged_in(self):
        self.assertFalse(
            AuthenticationManager()._logout(self.client)
        )