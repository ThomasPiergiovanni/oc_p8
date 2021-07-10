from django.test import TestCase

from authentication.tests.unit.models.test_custom_user import CustomUserTest


class SignOutViewTest(TestCase):
    """
    """  
    def test_get_with_redirect(self):
        response = self.client.get('/authentication/sign_out/', follow=True)
        self.assertEqual(response.redirect_chain[0][0], '/supersub/')