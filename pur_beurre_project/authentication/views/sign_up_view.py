from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authentication.forms.sign_up_form import SignUpForm
from authentication.managements.authentication_manager import (
    AuthenticationManager
)
from authentication.models import CustomUser
from supersub.views.custom_view import CustomView


class SignUpView(CustomView):
    """
    """
    def __init__(self):
        """
        """
        super().__init__()
        self.auth_manager = AuthenticationManager()
        self.data['redirect'] = 'authentication:sign_in'
        self.data['render'] = 'authentication/sign_up.html'

    def get(self, request):
        """
        """
        form = SignUpForm()
        self.data['ctxt']['form'] = form
        return render(request, self.data['render'], self.data['ctxt'])

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            self.auth_manager._create_user(form.cleaned_data)

            # CustomUser.objects.create_user(form.cleaned_data)
            #     email=form.cleaned_data['email'],
            #     password=form.cleaned_data['password1'],
            #     first_name=form.cleaned_data['first_name'])
            return HttpResponseRedirect(reverse(self.data['redirect']))
        else:
            self.data['ctxt']['form'] = form
            return render(request, self.data['render'], self.data['ctxt'])   