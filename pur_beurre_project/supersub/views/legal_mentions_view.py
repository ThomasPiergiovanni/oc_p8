from django.views import View
from django.shortcuts import render

from supersub.forms import NavbarSearchForm
from supersub.manager.supersub_manager import SupersubManager


class LegalMentionsView(View):
    """
    """
    def __init__(self):
        """
        """
        self.data = SupersubManager()._get_data()
        self.data['context']['navbar_form'] = NavbarSearchForm()
        self.data['render'] = 'supersub/legal_mentions.html'

    def get(self,request):
        """
        """
        return render(request, self.data['render'], self.data['context'] )