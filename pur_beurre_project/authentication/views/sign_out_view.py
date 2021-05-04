from django.contrib.auth import logout
from django.shortcuts import redirect

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
        logout(request)
        return redirect(self.data['redirect']) 