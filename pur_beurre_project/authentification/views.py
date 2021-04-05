from django.shortcuts import render

from authentification.user_session_manager import UserSessionManager

# Create your views here.

def account(request):
    user_session = UserSessionManager()
    if user_session.active:
        return render(request, 'authentification/account.html')
    else:
        # context ={
        #     'message': "Se connecter",
        #     'button_message': "Se connecter"
        # }
        return login(request)

def create_account(request):
    context ={
        'message': "Connection",
        'button_message': "Créer"
    }
    return render(request, 'authentification/create_account.html', context)

def login(request):
    context ={
        'message': "Se connecter",
        'button_message': "Se connecter"
    }
    return render(request, 'authentification/login.html', context)


