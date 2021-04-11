from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.utils.translation import gettext_lazy as _

from authentication.models import CustomUser


class SignUpForm(UserCreationForm):
    """
    """
    first_name = forms.CharField(label="Prénom", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # password2 = forms.CharField(label="Confirmer le mot de passe",widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['first_name', 'email', 'password1', 'password2']


class SignInForm(AuthenticationForm):
    """
    """
    class Meta(AuthenticationForm):
        model = CustomUser
        fields = ['email', 'password1']
    
