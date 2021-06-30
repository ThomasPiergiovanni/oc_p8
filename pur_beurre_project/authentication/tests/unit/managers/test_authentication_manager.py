from django.test import TestCase
from django.contrib.auth import authenticate

from authentication.models import CustomUser 
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
    
    def test_authenticate_with_email_and_password(self):
        self.assertTrue(
            AuthenticationManager()._authenticate('testuser@email.com','_Xxxxxxx')
        )

    def test_login_with_client_login(self):
        user = authenticate(
            email='testuser@email.com',
            password='_Xxxxxxx'
        )
        self.assertTrue(
            AuthenticationManager()._login(self.client, user)
        )
