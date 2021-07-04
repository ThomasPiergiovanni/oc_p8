from django.db import models
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
    
    def test_custom_user_with_instance(self):
        user = CustomUser.objects.get(pk=1)
        self.assertIsInstance(user, CustomUser)
        self.assertEquals(user.id, 1)
        self.assertEquals(user.email, 'testuser@email.com')
    
    def test__str__with_email(self):
        user = CustomUser.objects.get(pk=1)
        self.assertEqual(user.__str__(), 'testuser@email.com')