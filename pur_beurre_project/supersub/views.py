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
    def get(self,request):
        """
        """
        SupersubManager()._delete_session_variables(request)
        return render(request, 'supersub/index.html')


class ResutlView(View):
    """
    """
    def get(self, request):
        """
        """
        session_prod_id = request.session.get('session_prod_id', None)
        session_favs_cands_ids = request.session.get('session_favs_cands_ids', None)
        if session_favs_cands_ids:
            context = SupersubManager()._display_results_from_session_variables(request, session_prod_id, session_favs_cands_ids)
            return render(request, 'supersub/results.html', context)
        else:
            searched_string = request.GET.get('product', None)
            if searched_string:
                matching_products = Product.objects.filter(name__contains=searched_string)[:1]
                if matching_products:
                    context = SupersubManager()._display_results_from_form(request, matching_products) 
                    return render(request, 'supersub/results.html', context)
                else:
                    messages.add_message(request, messages.WARNING, "Ce produit n'a pas été reconnu ou n'existe pas.")
            else:
                messages.add_message(request, messages.ERROR, "Saisissez un produit")
            return HttpResponseRedirect(reverse('supersub:index'))


class ProductDetailView(View):
    """
    """
    def get(self, request, id_product):
        """
        """
        context = {
            'product': SupersubManager()._get_product(id_product)
        }
        return render(request, 'supersub/product_detail.html', context)


class FavoritesView(View):
    """
    """
    def get(self, request):
        if request.user.is_authenticated:
            favorites = list(
                Favorites.objects
                .filter(custom_user_id__exact=request.user.id)
                .select_related('product')
                .order_by('id'))
            if favorites:
                context = {
                    'page_object': SupersubManager()._paginate(
                        request, favorites)
                }
                return render(request, 'supersub/favorites.html', context)
            else:
                messages.add_message(request, messages.WARNING,"Vous n'avez enregistré aucun favoris jusqu'à présent")
        else:
            messages.add_message(request, messages.ERROR,"Connectez-vous pour consulter vos favoris!")
        return HttpResponseRedirect(reverse('supersub:index'))


class RegisterFavoriteView(View):
    """
    """
    def get(self, request, id_product, id_user):
        """
        """
        if SupersubManager()._get_favorite(id_product, id_user):
            messages.add_message(request, messages.WARNING,"Produit déja enregistré")
        else:
            Favorites(product_id=id_product, custom_user_id=id_user).save()
            messages.add_message(request, messages.SUCCESS,"Produit enregistré!")
        return HttpResponseRedirect(reverse('supersub:product_detail', args=[id_product]))
