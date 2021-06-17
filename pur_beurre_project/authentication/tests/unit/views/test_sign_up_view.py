from django.test import TestCase


from authentication.tests.unit.models.test_custom_user import CustomUserTest


class SignUpViewTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        CustomUserTest.emulate_custom_user()
    
    def test_get_with_status_code_200(self):
        self.response = self.client.get(
            '/authentication/sign_up/',
            follow=True)
        self.assertEqual(self.response.status_code, 200)