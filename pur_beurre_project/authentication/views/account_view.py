from django.shortcuts import render, redirect

from supersub.forms import NavbarSearchForm
from supersub.views.custom_view import CustomView


class AccountView(CustomView):
    """
    """
    def __init__(self):
        """
        """
        super().__init__()
        self.data['redirect'] = 'authentication:sign_in'
        self.data['render'] = 'authentication/account.html'

    def get(self, request):
        """
        """
        if not request.user.is_authenticated:
            return redirect(self.data['redirect'])
        else:
            self.data['ctxt']['user'] = request.user
            return render(request, self.data['render'], self.data['ctxt'])   