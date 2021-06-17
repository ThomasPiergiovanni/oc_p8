from django.test import TestCase

from authentication.forms.sign_up_form import SignUpForm
from authentication.tests.unit.models.test_custom_user import CustomUserTest
from supersub.forms.navbar_search_form import NavbarSearchForm


class SignUpViewTest(TestCase):
    """
    """
    def setUp(self):
        self.response_get = self.client.get('/authentication/sign_up/')
    
    def test_get_with_status_code_200(self):
        self.assertEqual(self.response_get.status_code, 200)
    
    def test_get_with_template(self):
        self.assertTemplateUsed(
            self.response_get, 'authentication/sign_up.html'
        )
    
    def test_get_with_form(self):
        self.assertIsInstance(
            self.response_get.context['form'], SignUpForm
        )
    
    def test_get_with_navbarform(self):
        self.assertIsInstance(
            self.response_get.context['navbar_form'], NavbarSearchForm
        )

    def test_post_with_redirect(self):
        response = self.client.post(
            '/authentication/sign_up/',
            data={
                'first_name': 'tester',
                'email': 'testuser@email.com',
                'password1':'_Xxxxxxx',
                'password2':'_Xxxxxxx'
            },
            follow=True
        )
        self.assertEqual(
            response.redirect_chain[0][0], '/authentication/sign_in/'
        )

    def test_post_with_render(self):
        response = self.client.post(
            '/authentication/sign_up/',
            data={
                'first_name': 'tester',
                'email': 'testuser@email.com',
                'password1':'rrr',
                'password2':'aaa'
            },
            follow=True
        ) 
        self.assertIsInstance(
            response.context['form'], SignUpForm
        )