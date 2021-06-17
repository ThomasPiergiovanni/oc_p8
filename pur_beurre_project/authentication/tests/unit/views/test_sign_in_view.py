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
