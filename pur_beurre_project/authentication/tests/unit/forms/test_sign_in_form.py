# pylint: disable=C0116
"""Test sign in form module (unitary test).
"""
from django.test import TestCase

from authentication.forms.sign_in_form import SignInForm
from authentication.tests.unit.models.test_custom_user import CustomUserTest


class SignInFormTest(TestCase):
    """Test sign in form class.
    """
    @classmethod
    def setUpTestData(cls):
        CustomUserTest.emulate_custom_user()

    def setUp(self):
        self.form = SignInForm()

    def test_signinform_with_attr_username_and_password_label(self):
        self.assertTrue(self.form.fields['username'].label == "Email")
        self.assertTrue(self.form.fields['password'].label == "Mot de passe")

    def test_signinform_with_attr_username_class(self):
        self.assertTrue(
            self.form.fields['username']
            .widget.attrs['class'] == 'form-control'
        )
        self.assertTrue(
            self.form.fields['password']
            .widget.attrs['class'] == 'form-control'
        )

    def test_signinform_with_attr_username_autofocus(self):
        self.assertTrue(
            self.form.fields['username']
            .widget.attrs['autofocus'] is True
        )

    def test_signinform_with_validation_wo_input(self):
        form = SignInForm(data={'username': '', 'password': ''})
        self.assertFalse(form.is_valid())

    def test_signinform_with_validation_wrong_input(self):
        form = SignInForm(
            data={
                'username': 'testuser@email.com',
                'password': '_ysssz'
            }
        )
        self.assertFalse(form.is_valid())

    def test_signinform_with_validation_with_input(self):
        form = SignInForm(
            data={
                'username': 'testuser@email.com',
                'password': '_Xxxxxxx'
            }
        )
        self.assertTrue(form.is_valid())
