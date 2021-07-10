from django.shortcuts import render, redirect

from authentication.forms.sign_in_form import SignInForm
from authentication.managements.authentication_manager import (
    AuthenticationManager
)
from supersub.views.custom_view import CustomView


class SignInView(CustomView):
    """
    """
    def __init__(self):
        """
        """
        super().__init__()
        self.auth_manager = AuthenticationManager()
        self.data['redirect'] = 'supersub:index'
        self.data['render'] = 'authentication/sign_in.html'

    def get(self, request):
        """
        """
        form = SignInForm()
        self.data['ctxt']['form'] = form
        return render(request, self.data['render'], self.data['ctxt'])
    
    def post(self, request):
        """
        """
        self.auth_manager._logout(request)
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = self.auth_manager._authenticate(form.cleaned_data)
            if user is not None:
                self.auth_manager._login(request, user)
                return redirect(self.data['redirect'])
        else:
            self.data['ctxt']['form'] = form
            return render(request, self.data['render'], self.data['ctxt'])