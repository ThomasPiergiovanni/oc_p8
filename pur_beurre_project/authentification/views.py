from django.shortcuts import render

# Create your views here.

def create_account(request):
    context ={
        'message': "Créer un compte",
        'button_message': "Créer"
    }
    return render(request, 'authentification/create_account.html', context)

def login(request):
    context ={
        'message': "Se connecter",
        'button_message': "Se connecter"
    }
    return render(request, 'authentification/login.html', context)


def account(request):
    return render(request, 'authentification/account.html')