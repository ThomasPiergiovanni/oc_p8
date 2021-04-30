from django import forms


class MainSearchForm(forms.Form):
    """
    """
    searched_string = forms.CharField(
        label=None,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autofocus': True}))

class NavbarSearchForm(forms.Form):
    """
    """
    searched_string = forms.CharField(
        label=None,
        widget=forms.TextInput(attrs={
            'class': 'form-control mybox'}))