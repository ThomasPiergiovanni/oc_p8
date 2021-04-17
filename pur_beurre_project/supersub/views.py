from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Product, Favorites
from authentication.models import CustomUser



# Create your views here.
def index(request):
    return render(request, 'supersub/index.html')

def product_detail(request, id_product):
    product = Product.objects.get(pk=id_product)
    context = {
        'product': product
    }
    return render(request, 'supersub/product_detail.html', context)


def registered_products(request):
    user = request.user
    if user.is_authenticated:
        entry_list = list(Favorites.objects.filter(custom_user_id__exact=user.id)) 
        if entry_list:
            favorites = Favorites.objects.filter(custom_user_id__exact=user.id).select_related('product')
            context = {
                'favorites': favorites
            }
            return render(request, 'supersub/registered_products.html', context)
        else:
            context = {
                'message': " Vous n'avez enregistré aucun favoris jusqu'à présent"
            }
            return render(request, 'supersub/index.html', context)
    else:
            context = {
                'message': " Vous devez vous connecter pour consulter vos favoris"
            }
            return render(request, 'supersub/index.html', context)

def register_product(request, id_product, id_user):
    product = Product.objects.get(pk=id_product)
    try:
        favorite = Favorites.objects.get(product_id__exact=id_product, custom_user_id__exact=id_user)
        if favorite is not None:
            context = {
                'product': product,
                'message': "Ce produit fait déja parti de vos favoris"
            }
            return render(request, 'supersub/product_detail.html', context)
    except:
        favorite = Favorites(product_id=id_product, custom_user_id=id_user)
        favorite.save()
        context = {
                    'product': product,
                    'favorite_message': "Ce produit a été ajouté vos favoris"
                }
        return render(request, 'supersub/product_detail.html', context)

def results(request):
    """
    """
    if request.method == 'GET':
        try:
            matching_products = Product.objects.filter(name__contains=request.GET['product'])
            product = matching_products[0]
            products_list = (
                Product.objects.filter(category_id=product.category_id)
                .filter(nutriscore_grade__lte=product.nutriscore_grade)
                .exclude(id__exact=product.id).order_by('id')[:6]
            )
            context = {
                'searched_product': product,
                'products': products_list

            }
            return render(request, 'supersub/results.html', context)
        except:
            context = {
                'message': "Ce produit n'a pas été reconnu ou n'existe pas dans la base de donnée. Faites une nouvelle recherche"
            }
            return render(request, 'supersub/index.html', context)