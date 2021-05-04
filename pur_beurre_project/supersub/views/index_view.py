from django.shortcuts import render

from supersub.forms import MainSearchForm, NavbarSearchForm
from supersub.views.custom_view import CustomView


class IndexView(CustomView):
    """
    """
    def __init__(self):
        """
        """
        super().__init__()
        self.data['render'] = 'supersub/index.html'

    def get(self,request):
        """
        """
        self.manager._delete_session_vars(request)
        return render(request, self.data['render'], self.data['ctxt'])