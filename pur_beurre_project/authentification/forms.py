from django import forms


class CreateAccountForm(forms.Form):
    """
    """
    first_name = forms.CharField(label='Prénom', widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class LoginForm(forms.Form):
    """
    """
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
