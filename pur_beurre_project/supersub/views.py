from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request, 'supersub/index.html')

# def account(request):
#     return render(request, 'supersub/account.html')

def aliment(request):
    return render(request, 'supersub/aliment.html')

def create_account(request):
    context ={
        'message': "Créer un compte",
        'button_message': "Créer"
    }
    return render(request, 'supersub/create_account.html', context)

def login(request):
    context ={
        'message': "Se connecter",
        'button_message': "Se connecter"
    }
    return render(request, 'supersub/login.html', context)

def registered_aliments(request):
    return render(request, 'supersub/registered_aliments.html')

def results(request):
    return render(request, 'supersub/results.html')