"""Accout view module.
"""
from django.shortcuts import render, redirect

from supersub.views.custom_view import CustomView


class AccountView(CustomView):
    """Accout view class.
    """
    def __init__(self):
        super().__init__()
        self._data['redirect'] = 'authentication:sign_in'
        self._data['render'] = 'authentication/account.html'

    def get(self, request):
        """Account view method on client get request. View is dipslayed if the
        user is authenticated.
        """
        if not request.user.is_authenticated:
            return redirect(self._data['redirect'])
        self._data['ctxt']['user'] = request.user
        return render(request, self._data['render'], self._data['ctxt'])
