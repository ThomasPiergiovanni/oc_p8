from django.contrib.auth import authenticate
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory, TestCase

from authentication.managers.authentication_manager import AuthenticationManager
from authentication.tests.unit.models.test_custom_user import CustomUserTest


class AuthenticationManagerTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        CustomUserTest.emulate_custom_user()
        cls.auth_manager = AuthenticationManager()
    
    def setUp(self):
        pass

    def test_logout_with_client_logged_in(self):
        self.client.login(
            email='testuser@email.com',
            password='_Xxxxxxx'
        )
        self.assertFalse(
            self.auth_manager._logout(self.client)
        )
    
    def test_authenticate_with_email_and_password(self):
        self.assertTrue(
            self.auth_manager._authenticate('testuser@email.com','_Xxxxxxx')
        )

    def test_login_with_client_login(self):
        request = RequestFactory().post('')
        session_middleware = SessionMiddleware()
        session_middleware.process_request(request)
        user = authenticate(email='testuser@email.com', password='_Xxxxxxx' )
        self.auth_manager._login(request, user)
        self.assertEqual(request.session.get('_auth_user_id'), "1")
