# pylint: disable=
"""Sign up form module.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm

from authentication.models import CustomUser


class SignUpForm(UserCreationForm):
    """Sign up form class.
    """
    first_name = forms.CharField(
        label="Prénom",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autofocus': True,
                'id': 'id_first_name_input'
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'id_email_input'
            }
        )
    )
    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'id_pwd1_input'
            }
        )
    )
    password2 = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'id_pwd2_input'
            }
        )
    )

    class Meta(UserCreationForm):
        """Meta model gives CustomUser "params" to Signupform lcass.
        """
        model = CustomUser
        fields = ['first_name', 'email', 'password1', 'password2']
