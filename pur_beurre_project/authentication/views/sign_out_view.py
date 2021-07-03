from django.contrib.auth import logout
from django.shortcuts import redirect

from authentication.managements.authentication_manager import (
    AuthenticationManager
)
from supersub.views.custom_view import CustomView


class SignOutView(CustomView):
    """
    """
    def __init__(self):
        """
        """
        super().__init__()
        self.data['redirect'] = 'supersub:index'

    def get(self, request):
        """
        """
        AuthenticationManager()._logout(request)
        return redirect(self.data['redirect']) 