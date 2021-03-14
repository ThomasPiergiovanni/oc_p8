from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request, 'supersub/index.html')

def results(request):
    return render(request, 'supersub/results.html')

def account(request):
    return render(request, 'supersub/account.html')

def aliment(request):
    return render(request, 'supersub/aliment.html')
