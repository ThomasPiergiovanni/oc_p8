from django.shortcuts import render
from supersub.forms import MainSearchForm, NavbarSearchForm
from supersub.manager.supersub_manager import SupersubManager
from django.views import View


class IndexView(View):
    """
    """
    def __init__(self):
        """
        """
        self.data = SupersubManager()._get_data()
        self.data['context']['main_form'] = MainSearchForm()
        self.data['context']['navbar_form'] = NavbarSearchForm()
        self.data['render'] = 'supersub/index.html'

    def get(self,request):
        """
        """
        SupersubManager()._delete_session_variables(request)
        return render(request, self.data['render'], self.data['context'])