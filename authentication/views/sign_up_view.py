# pylint: disable=W0212
"""Sign up view module.
"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authentication.forms.sign_up_form import SignUpForm
from authentication.management.authentication_manager import (
    AuthenticationManager
)
from supersub.views.custom_view import CustomView


class SignUpView(CustomView, AuthenticationManager):
    """Sign up view class.
    """
    def __init__(self):
        super().__init__()
        self._data['redirect'] = 'authentication:sign_in'
        self._data['render'] = 'authentication/sign_up.html'

    def get(self, request):
        """Sign up view method on client get request.
        """
        form = SignUpForm()
        self._data['ctxt']['form'] = form
        return render(request, self._data['render'], self._data['ctxt'])

    def post(self, request):
        """Sign up view method on client post request. If the user is not
        present in DB and the form provided info are ok, the user is
        redirected to the sign in page. If any of those criteria is not met,
        the same page is rendered to the user.
        """
        form = SignUpForm(request.POST)
        if form.is_valid():
            self._create_user(form.cleaned_data)
            return HttpResponseRedirect(reverse(self._data['redirect']))
        self._data['ctxt']['form'] = form
        return render(request, self._data['render'], self._data['ctxt'])
