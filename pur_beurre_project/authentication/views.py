from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from authentication.models import CustomUser
from authentication.forms import SignUpForm, SignInForm

from supersub.manager.supersub_manager import SupersubManager
from supersub.forms import NavbarSearchForm



# Create your views here.


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


class SignInView(View):
    """
    """
    def get(self, request):
        """
        """
        form = SignInForm()
        context = {
            'form' : form
        }
        return render(request, 'authentication/sign_in.html', context)
    
    def post(self, request):
        """
        """
        logout(request)
        form = SignInForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('supersub:index')
        else:
            context = {
                'form' : form
            }
            return render(request, 'authentication/sign_in.html', context)


class SignOutView(View):
    """
    """
    def get(self, request):
        """
        """
        logout(request)
        return redirect('supersub:index') 