from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authentication.user_session import UserSession
from authentication.models import User
from authentication.forms import CreateAccountForm, LoginForm

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


def create_account(request):
    """
    """
    if request.method == 'POST':
        create_account_form = CreateAccountForm(request.POST)
        if create_account_form.is_valid():
            first_name = create_account_form.cleaned_data['first_name']
            email = create_account_form.cleaned_data['email']
            password1 = create_account_form.cleaned_data['password1']
            password2 = create_account_form.cleaned_data['password2']
            try:
                user = User(
                first_name=first_name,
                email=email,
                password=password1
                )
                user.save()
                return HttpResponseRedirect(reverse('supersub:index'))
            except:
                create_account_form = CreateAccountForm()
                context = {
                    'form' : create_account_form
                }
                return render(request, 'authentication/create_account.html', context)
        else:
            context = {
                'form' : create_account_form
            }
            return render(request, 'authentication/create_account.html', context)

            
    else:
        create_account_form = CreateAccountForm()
        context = {
            'form' : create_account_form
        }
        return render(request, 'authentication/create_account.html', context) 

# def login(request):
#     """
#     """
#     if request.method == 'POST':
#         if request.method == 'POST':
#     context ={
#         'message': "Se connecter",
#         'button_message': "Se connecter"
#     }
#     return render(request, 'authentification/login.html', context)

def login(request):
    """
    """
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            try:
                existing_user = User.objects.get(email__iexact=email, password__iexact=password)
                return render(request, 'supersub/index.html')
            except:
                login_form = LoginForm()
                context = {
                    'login_form' : login_form,
                    'error_message': "Email et/ou mot de passe incorrect"
                }
                return render(request, 'authentication/login.html', context)
        else:
            login_form = LoginForm()
            context = {
                'login_form' : login_form,
                'error_message': "L\'adresse email n'est pas valide"
            }
            return render(request, 'authentication/login.html', context)
    else:
        login_form = LoginForm()
        context = {
            'login_form' : login_form
        }
        return render(request, 'authentication/login.html', context) 


