from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authentification.user_session_manager import UserSessionManager
from authentification.models import User
from authentification.forms import CreateAccountForm

# Create your views here.

def account(request):
    user_session = UserSessionManager()
    if user_session.active:
        return render(request, 'authentification/account.html')
    else:
        return login(request)


def create_account(request):

    if request.method == 'POST':
        create_account_form = CreateAccountForm(request.POST)
        if create_account_form.is_valid():
            first_name = create_account_form.cleaned_data['first_name']
            email = create_account_form.cleaned_data['email']
            password = create_account_form.cleaned_data['password']
            try:
                existing_user = User.objects.get(email__iexact=email)
                context = {
                    'create_account_form' : create_account_form,
                    'error_message': " est déja utilisé. Choissisez un autre nom.",
                    'email': existing_user.email
                }
                return render(request, 'authentification/create_account.html', context)
            except:
                user = User(
                    first_name=first_name,
                    email=email,
                    password=password
                )
                user.save()
                context = {
                    'create_account_form' : create_account_form,
                    'error_message': " n'est pas utilisé et a été créer",
                    'email': email,
                }
                return HttpResponseRedirect(reverse('supersub:index'))
    else:
        create_account_form = CreateAccountForm()
        context = {
            'create_account_form' : create_account_form
        }
        return render(request, 'authentification/create_account.html', context) 

def login(request):
    """
    """
    context ={
        'message': "Se connecter",
        'button_message': "Se connecter"
    }
    return render(request, 'authentification/login.html', context)


