from django.views import View

from supersub.forms import MainSearchForm, NavbarSearchForm
from supersub.manager.supersub_manager import SupersubManager

class CustomView(View):
    """
    """
    def __init__(self):
        """
        """
        self.data = SupersubManager()._get_data()
        self.data['context']['main_form'] = MainSearchForm()
        self.data['context']['navbar_form'] = NavbarSearchForm()
        self.data['context']['searched_product'] = ''
        self.data['context']['product'] = ''
        self.data['context']['page_object'] = ''
        self.data['render'] = ''
        self.data['redirect'] = ''