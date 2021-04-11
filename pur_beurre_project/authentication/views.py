from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authentication.models import CustomUser
from authentication.forms import SignInForm, LoginForm

# Create your views here.

def account(request):
    pass
#     user_session = UserSession()
#     if user_session.active:
#         context = {
#             'user_session':user_session
#         }
#         return render(request, 'authentification/account.html', context)
#     else:
#         return login(request)


def signin(request):
    """
    """
    if request.method == 'POST':
        signin_form = SignInForm(request.POST)
        if signin_form.is_valid():
            first_name = signin_form.cleaned_data['first_name']
            email = signin_form.cleaned_data['email']
            password1 = signin_form.cleaned_data['password1']
            password2 = signin_form.cleaned_data['password2']
            user = CustomUser.objects.create_user(
                email=email,
                password=password1,
                first_name=first_name)
            # user = authenticate(email=user.email, password=user.password)
            # if user is not None:
            return HttpResponseRedirect(reverse('supersub:index'))
        else:
            context = {
                'form' : signin_form
            }
            return render(request, 'authentication/signin.html', context)   
    else:
        signin_form = SignInForm()
        context = {
            'form' : signin_form
        }
        return render(request, 'authentication/signin.html', context) 


def login(request):
    """
    """
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            return HttpResponseRedirect(reverse('supersub:index'))
        else:
            context = {
                'form' : login_form
            }
            return render(request, 'authentication/login.html', context)
    else:
        login_form = LoginForm()
        context = {
            'form' : login_form
        }
        return render(request, 'authentication/login.html', context) 


