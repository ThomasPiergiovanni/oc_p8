from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from authentication.models import CustomUser
from authentication.forms import SignUpForm
from supersub.manager.supersub_manager import SupersubManager
from supersub.forms import NavbarSearchForm


# Create your views here.


class SignUpView(View):
    """
    """
    def __init__(self):
        """
        """
        self.data = SupersubManager()._get_data()
        self.data['context']['navbar_form'] = NavbarSearchForm()
        self.data['context']['form'] = ""
        self.data['redirect'] = 'authentication:sign_in'
        self.data['render'] = 'authentication/sign_up.html'

    def get(self, request):
        """
        """
        form = SignUpForm()
        self.data['context']['form'] = form
        return render(request, self.data['render'], self.data['context'])

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create_user(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
                first_name=form.cleaned_data['first_name'])
            return HttpResponseRedirect(reverse(self.data['redirect']))
        else:
            self.data['context']['form'] = form
            return render(request, self.data['render'], self.data['context'])   