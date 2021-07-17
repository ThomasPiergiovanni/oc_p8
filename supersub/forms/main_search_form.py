"""Main search form module
"""
from django import forms


class MainSearchForm(forms.Form):
    """Main search form class. Used for searching product substitute
    """
    product = forms.CharField(
        label=None,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autofocus': True,
                'id': 'id_main_form'
            }
        )
    )
