from django import forms


class MainSearchForm(forms.Form):
    """
    """
    product = forms.CharField(
        label=None,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autofocus': True}))

class NavbarSearchForm(forms.Form):
    """
    """
    product = forms.CharField(
        label=None,
        widget=forms.TextInput(attrs={
            'class': 'form-control mybox'}))