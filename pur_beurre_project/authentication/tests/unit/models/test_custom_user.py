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
    
    def test_custom_user_with_attr_username(self):
        user_field = CustomUser._meta.get_field('email')
        self.assertTrue(user_field)
        self.assertEquals(type(user_field), type(models.EmailField()))
        self.assertEquals(user_field.max_length, 250)
        self.assertEquals(user_field.unique, True)
    
    def test_custom_user_with_attr_first_name(self):
        user_field = CustomUser._meta.get_field('first_name')
        self.assertTrue(user_field)
        self.assertEquals(type(user_field), type(models.TextField()))
        self.assertEquals(user_field.max_length, 100)
        self.assertEquals(user_field.null, False)