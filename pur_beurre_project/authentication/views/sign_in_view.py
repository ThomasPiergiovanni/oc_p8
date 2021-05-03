from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from authentication.forms import SignInForm

from supersub.manager.supersub_manager import SupersubManager
from supersub.forms import NavbarSearchForm


# Create your views here.


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