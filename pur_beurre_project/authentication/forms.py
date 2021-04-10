from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.utils.translation import gettext_lazy as _

from authentication.models import User


class CreateAccountForm(UserCreationForm):
    """
    """
    first_name = forms.CharField(label="Prénom", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirmer le mot de passe",widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta(UserCreationForm):
        model = User
        fields = ['first_name', 'email', 'password1', 'password2' ]


class LoginForm(UserCreationForm):
    """
    """
    pass
    
    # email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    # password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
