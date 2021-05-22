from django.test import TestCase

from authentication.models import CustomUser

class CustomUserTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        cls.emulate_custom_user()
    
    @classmethod
    def emulate_custom_user(cls):
        custom_user = CustomUser.objects.create_user(
                id=1,
                email='testuser@email.com',
                password='_Xxxxxxx',
                first_name='tester')