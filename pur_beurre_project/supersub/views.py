from django.contrib import messages
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
    def __init__(self):
        self.supersub_manager = SupersubManager()

    def get(self,request):
        """
        """
        self.supersub_manager._delete_session_variables(request)
        return render(request, 'supersub/index.html')


class ProductDetailView(View):
    """
    """
    def get(self, request, id_product):
        product = Product.objects.get(pk=id_product)
        context = {
            'product': product
        }
        return render(request, 'supersub/product_detail.html', context)


class FavoritesView(View):
    """
    """
    def __init__(self):
        """
        """
        self.supersub_manager = SupersubManager()

    def get(self, request):
        if request.user.is_authenticated:
            if list(
                    Favorites.objects
                    .filter(custom_user_id__exact=request.user.id)):
                favorites = (
                    Favorites.objects
                    .filter(custom_user_id__exact=request.user.id)
                    .select_related('product')
                    .order_by('id'))
                context = {
                    'page_object': self.supersub_manager._paginate(
                        request, favorites)
                }
                return render(request, 'supersub/favorites.html', context)
            else:
                messages.add_message(request, messages.WARNING,"Vous n'avez enregistré aucun favoris jusqu'à présent")
        else:
            messages.add_message(request, messages.ERROR,"Connectez-vous pour consulter vos favoris!")
        return render(request, 'supersub/index.html')



class RegisterFavoriteView(View):
    """
    """
    def __init__(self):
        """
        """
        self.supersub_manager = SupersubManager()
 
    def get(self, request, id_product, id_user):
        """
        """
        if self.supersub_manager._get_favorite(id_product, id_user):
            messages.add_message(request, messages.WARNING,"Produit déja enregistré")
        else:
            Favorites(product_id=id_product, custom_user_id=id_user).save()
            messages.add_message(request, messages.SUCCESS,"Produit enregistré!")
        return HttpResponseRedirect(reverse('supersub:product_detail', args=[id_product]))


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
                'page_object' : self.supersub_manager._paginate(request, candidates_favorites)
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
                    
                    self.supersub_manager._add_variables_to_session(
                        request, product_id, candidates_favorites_ids
                    )
                    context = {
                        'searched_product': product,
                        'page_object' : self.supersub_manager._paginate(
                            request, candidates_favorites
                        )
                    }
                    return render(request, 'supersub/results.html', context)
            messages.add_message(request, messages.ERROR, "Ce produit n'a pas été reconnu ou n'existe pas dans la base de donnée.")
            return HttpResponseRedirect(reverse('supersub:index'))
