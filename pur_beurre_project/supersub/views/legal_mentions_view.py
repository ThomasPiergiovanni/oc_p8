from django.shortcuts import render

from supersub.forms import NavbarSearchForm
from supersub.manager.supersub_manager import SupersubManager
from supersub.views.custom_view import CustomView


class LegalMentionsView(CustomView):
    """
    """
    def __init__(self):
        """
        """
        super().__init__()
        self.data['render'] = 'supersub/legal_mentions.html'

    def get(self,request):
        """
        """
        return render(request, self.data['render'], self.data['context'] )