""" Custom view module
"""
from django.views import View

from supersub.forms.main_search_form import MainSearchForm
from supersub.forms.navbar_search_form import NavbarSearchForm
from supersub.management.app.supersub_manager import SupersubManager


class CustomView(View):
    """Custom view class
    """
    def __init__(self):
        super().__init__()
        self.manager = SupersubManager()
        self.data = SupersubManager()._get_data()
        self.data['ctxt']['main_form'] = MainSearchForm()
        self.data['ctxt']['navbar_form'] = NavbarSearchForm()
        self.data['ctxt']['searched_prod'] = ''
        self.data['ctxt']['prod'] = ''
        self.data['ctxt']['page_obj'] = ''
        self.data['ctxt']['user'] = ''
        self.data['ctxt']['form'] = ''
        self.data['render'] = ''
        self.data['redirect'] = ''
