from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request, 'supersub/index.html')

def account(request):
    return render(request, 'supersub/account.html')

def aliment(request):
    return render(request, 'supersub/aliment.html')

def create_account(request):
    return render(request, 'supersub/create_account.html')

def results(request):
    return render(request, 'supersub/results.html')