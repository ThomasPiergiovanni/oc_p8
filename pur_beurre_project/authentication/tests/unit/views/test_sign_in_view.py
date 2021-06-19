from django.test import TestCase

from authentication.forms.sign_in_form import SignInForm
from authentication.tests.unit.models.test_custom_user import CustomUserTest
from supersub.forms.navbar_search_form import NavbarSearchForm


class SignInViewTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        CustomUserTest.emulate_custom_user()

    def setUp(self):
        self.response_get = self.client.get('/authentication/sign_in/')

    def test_get_with_status_code_200(self):
        self.assertEqual(self.response_get.status_code, 200)
    
    def test_get_with_template(self):
        self.assertTemplateUsed(
            self.response_get, 'authentication/sign_in.html'
        )

    def test_get_with_form(self):
        self.assertIsInstance(
            self.response_get.context['form'], SignInForm
        )

    def test_get_with_navbarform(self):
        self.assertIsInstance(
            self.response_get.context['navbar_form'], NavbarSearchForm
        )
    
    def test_post_with_redirect(self):
        response = self.client.post(
            '/authentication/sign_in/',
            data={
                'username': 'testuser@email.com',
                'password': '_Xxxxxxx'
            },
            follow=True
        )
        self.assertEqual(
            response.redirect_chain[0][0], '/supersub/'
        )

    def test_post_with_render(self):
        response = self.client.post(
            '/authentication/sign_in/',
            data={
                'username': 'noexists@email.com',
                'password': '_Yyyyyyy'
            },
            follow=True
        )
        self.assertIsInstance(
            response.context['form'], SignInForm
        )