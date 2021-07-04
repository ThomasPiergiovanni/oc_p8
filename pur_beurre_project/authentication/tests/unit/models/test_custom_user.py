from django.db import models
from django.test import TestCase

from authentication.models import CustomUser

class CustomUserTest(TestCase):
    """
    """
    def test_custom_user_with_attr_username(self):
        user_field = CustomUser._meta.get_field('email')
        self.assertTrue(user_field)
        self.assertEqual(type(user_field), type(models.EmailField()))
        self.assertEqual(user_field.max_length, 250)
        self.assertEqual(user_field.unique, True)
    
    def test_custom_user_with_attr_first_name(self):
        user_field = CustomUser._meta.get_field('first_name')
        self.assertTrue(user_field)
        self.assertEqual(type(user_field), type(models.TextField()))
        self.assertEqual(user_field.max_length, 100)
        self.assertEqual(user_field.null, False)
