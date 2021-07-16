""" Custom view module
"""
from django.views import View

from supersub.forms.main_search_form import MainSearchForm
from supersub.forms.navbar_search_form import NavbarSearchForm
from supersub.management.app.supersub_manager import SupersubManager


class CustomView(View, SupersubManager):
    """Custom view class
    """
    def __init__(self):
        super().__init__()
        self._data = self._get_data()
        self._data['ctxt']['main_form'] = MainSearchForm()
        self._data['ctxt']['navbar_form'] = NavbarSearchForm()
        self._data['ctxt']['searched_prod'] = ''
        self._data['ctxt']['prod'] = ''
        self._data['ctxt']['page_obj'] = ''
        self._data['ctxt']['user'] = ''
        self._data['ctxt']['form'] = ''
        self._data['render'] = ''
        self._data['redirect'] = ''
