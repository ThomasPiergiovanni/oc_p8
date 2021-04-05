from django.shortcuts import render

# Create your views here.

def account(request):
    return render(request, 'authentification/account.html')

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


