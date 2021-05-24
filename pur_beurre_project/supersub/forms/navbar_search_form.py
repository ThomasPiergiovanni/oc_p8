from django import forms


class NavbarSearchForm(forms.Form):
    """
    """
    product = forms.CharField(
        label=None,
        widget=forms.TextInput(attrs={
            'class': 'form-control mybox'}))