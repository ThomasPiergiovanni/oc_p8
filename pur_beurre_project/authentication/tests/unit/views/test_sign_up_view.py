from django.test import TestCase

from authentication.forms.sign_up_form import SignUpForm
from authentication.tests.unit.models.test_custom_user import CustomUserTest
from supersub.forms.navbar_search_form import NavbarSearchForm


class SignUpViewTest(TestCase):
    """
    """
    def setUp(self):
        self.response = self.client.get('/authentication/sign_up/')
    
    def test_get_with_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_get_with_template(self):
        self.assertTemplateUsed(self.response, 'authentication/sign_up.html')
    
    def test_get_with_form(self):
        self.assertIsInstance(
            self.response.context['form'], SignUpForm
        )
    
    def test_get_with_navbarform(self):
        self.assertIsInstance(
            self.response.context['navbar_form'],
            NavbarSearchForm
        )