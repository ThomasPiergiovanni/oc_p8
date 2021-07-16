# pylint: disable=W0212
"""Sign out view module.
"""
from django.shortcuts import redirect

from authentication.management.authentication_manager import (
    AuthenticationManager
)
from supersub.views.custom_view import CustomView


class SignOutView(CustomView, AuthenticationManager):
    """Sign out view class.
    """
    def __init__(self):
        super().__init__()
        self._data['redirect'] = 'supersub:index'

    def get(self, request):
        """Sign out method on client get request. After logging the user
        out, the user is redirected to the index page.
        """
        self._logout(request)
        return redirect(self._data['redirect'])
