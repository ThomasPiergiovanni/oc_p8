from django.forms import ModelForm

from authentification.models import User


class UserForm(ModelForm):
    """
    """
    class Meta:
        model = User
        fields = ['first_name', 'email', 'password']
        widget = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'id': 'create_account_first_name',
                'name': 'create_account_first_name',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'id': 'create_account_email',
                'name': 'create_account_email',
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'id': 'create_account_password',
                'name': 'create_account_password',
            }),
        }