from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Product, Favorites
from authentication.models import CustomUser
from .manager.supersub_manager import SupersubManager

from django.views import View

from django.views.generic import DetailView


class IndexView(View):
    """
    """
    def get(self,request):
        try:
            del request.session['product_id']
            del request.session['candidates_favorites_ids']
            return render(request, 'supersub/index.html')
        except:
            return render(request, 'supersub/index.html')


class ProductDetailView(View):

    def get(self, request, id_product):
        product = Product.objects.get(pk=id_product)
        context = {
            'product': product
        }
        return render(request, 'supersub/product_detail.html', context)


class FavoritesView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            entry_list = list(Favorites.objects.filter(custom_user_id__exact=user.id)) 
            if entry_list:
                favorites = Favorites.objects.filter(custom_user_id__exact=user.id).select_related('product').order_by('id')
                context = {
                    'page_object': paginate(request, favorites)
                }
                return render(request, 'supersub/favorites.html', context)
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


class RegisterFavoriteView(View):
    """
    """
    def __init__(self):
        self.favorite = None
    
    def get(self, request, id_product, id_user):
        """
        """
        product = Product.objects.get(pk=id_product)
        try:
            self.favorite = Favorites.objects.get(product_id__exact=id_product, custom_user_id__exact=id_user)
            if self.favorite is not None:
                context = {
                    'product': product,
                    'message': "Ce produit fait déja parti de vos favoris"
                }
                return render(request, 'supersub/product_detail.html', context)
    
        except:
            self.favorite = Favorites(product_id=id_product, custom_user_id=id_user)
            self.favorite.save()
            context = {
                        'product': product,
                        'message': "Ce produit a été ajouté vos favoris"
                    }
            return render(request, 'supersub/product_detail.html', context)


class ResutlView(View):
    """
    """
    def __init__(self):
        """
        """
        self.supersub_manager = SupersubManager()

    def get(self, request):
        product_id = request.session.get('product_id', None)
        candidates_favorites_ids = request.session.get('candidates_favorites_ids', None)
        if candidates_favorites_ids:
            candidates_favorites = []
            for candidate_favorite_id in candidates_favorites_ids:
                product = Product.objects.get(pk=candidate_favorite_id)
                candidates_favorites.append(product)
            product = Product.objects.get(pk=product_id)
            context = {
                'searched_product': product,
                'page_object' : self.supersub_manager.paginate(request, candidates_favorites)
            }
            return render(request, 'supersub/results.html', context)
        else:
            searched_string = request.GET.get('product', None)
            if searched_string:
                matching_products = Product.objects.filter(name__contains=searched_string)
                if matching_products:
                    product = matching_products[0]
                    product_id = product.id
                    candidates_favorites_ids = []
                    candidates_favorites = (
                        Product.objects.filter(category_id=product.category_id)
                        .filter(nutriscore_grade__lte=product.nutriscore_grade)
                        .exclude(id__exact=product.id).order_by('id')
                    )
                    for candidate in candidates_favorites:
                        candidates_favorites_ids.append(candidate.id)
                    
                    self.supersub_manager.add_variables_to_session(request=request, product_id=product_id, candidates_favorites_ids=candidates_favorites_ids)
                    context = {
                        'searched_product': product,
                        'page_object' : self.supersub_manager.paginate(request, candidates_favorites)
                    }
                    return render(request, 'supersub/results.html', context)
                else:
                    context = {
                        'message': "Ce produit n'a pas été reconnu ou n'existe pas dans la base de donnée. Faites une nouvelle recherche"
                    }
                    return render(request, 'supersub/index.html', context)
            else:
                context = {
                    'message': "Ce produit n'a pas été reconnu ou n'existe pas dans la base de donnée. Faites une nouvelle recherche"
                }
                return render(request, 'supersub/index.html', context)
