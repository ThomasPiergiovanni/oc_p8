from django.shortcuts import render, redirect
from django.views import View

from supersub.manager.supersub_manager import SupersubManager
from supersub.forms import NavbarSearchForm


class AccountView(View):
    """
    """
    def __init__(self):
        """
        """
        self.data = SupersubManager()._get_data()
        self.data['context']['navbar_form'] = NavbarSearchForm()
        self.data['context']['user'] = ""
        self.data['redirect'] = 'authentication:sign_in'
        self.data['render'] = 'authentication/account.html'

    def get(self, request):
        """
        """
        if not request.user.is_authenticated:
            return redirect(self.data['redirect'])
        else:
            self.data['context']['user'] = request.user
            return render(request, self.data['render'], self.data['context'])   