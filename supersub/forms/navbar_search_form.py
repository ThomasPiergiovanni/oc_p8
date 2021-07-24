"""Navigation bar search form module
"""
from django import forms


class NavbarSearchForm(forms.Form):
    """Navigation bar search form class. Used for searching product substitute
    with the navbar form
    """
    product = forms.CharField(
        label=None,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mybox',
                'autofocus': False
            }
        )
    )
