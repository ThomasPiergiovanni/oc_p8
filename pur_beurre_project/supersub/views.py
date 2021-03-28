from django.shortcuts import get_object_or_404, render

from .models import Product



# Create your views here.
def index(request):
    return render(request, 'supersub/index.html')

# def account(request):
#     return render(request, 'supersub/account.html')

def aliment(request):
    return render(request, 'supersub/aliment.html')


def registered_aliments(request):
    return render(request, 'supersub/registered_aliments.html')

def results(request):
    return render(request, 'supersub/results.html', context)

def test_results(request):
    selected_id = request.POST['product_id']
    context = {
        'product': selected_id
    }
    return render(request, 'supersub/test_results.html', context)