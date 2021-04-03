from django.shortcuts import get_object_or_404, render

from .models import Product



# Create your views here.
def index(request):
    return render(request, 'supersub/index.html')

# def account(request):
#     return render(request, 'supersub/account.html')

def aliment(request, id_product):
    product = Product.objects.get(pk=id_product)
    context = {
        'name': product.name,
        'nutriscore_grade': product.nutriscore_grade,
        'fat': product.fat,
        'saturated_fat': product.saturated_fat,
        'sugar': product.sugar,
        'salt': product.salt,
        'image': product.image
    }

    return render(request, 'supersub/aliment.html', context)


def registered_aliments(request):
    return render(request, 'supersub/registered_aliments.html')


def results(request):
    """
    """
    try:
        products = Product.objects.filter(name__contains=request.POST['product'])
        product = products[0]
        products_in_catgeories = (
            Product.objects.filter(category_id=product.category_id)
            .filter(nutriscore_grade__lte=product.nutriscore_grade)
            .exclude(id__exact=product.id)[:6]
        )
        context = {
            'name': product.name,
            'image': product.image,
            'products_in_categories': products_in_catgeories
        }
        return render(request, 'supersub/results.html', context)
    except:
        context = {
            'error_message': "Ce produit n'a pas été reconnu ou n'existe pas dans la base de donnée. Faites une nouvelle recherche"
        }
        return render(request, 'supersub/index.html', context)
