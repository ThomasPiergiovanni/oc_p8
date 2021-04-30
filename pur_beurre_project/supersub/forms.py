from django import forms


class SearchForm(forms.Form):
    """
    """
    searched_string = forms.CharField(
        label=None,
        widget=forms.TextInput(attrs={
            'class': 'form-control mybox',
            'autofocus': True}))