from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _

from authentication.models import User


class CreateAccountForm(UserCreationForm):
    """
    """
    class Meta(UserCreationForm):
        model = User
        fields = ['first_name', 'email', 'password1', 'password2' ]
    
        
    # first_name = forms.CharField(label='Prénom', widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    # email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    # password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class LoginForm(UserCreationForm):
    """
    """
    pass
    
    # email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    # password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
