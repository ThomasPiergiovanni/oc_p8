from django.views import View

from supersub.forms import MainSearchForm, NavbarSearchForm
from supersub.manager.supersub_manager import SupersubManager

class CustomView(View):
    """
    """
    def __init__(self):
        """
        """
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