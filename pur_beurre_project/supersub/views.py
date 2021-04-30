from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Product, Favorites
from authentication.models import CustomUser
from .forms import MainSearchForm, NavbarSearchForm
from .manager.supersub_manager import SupersubManager

from django.views import View


class IndexView(View):
    """
    """
    def get(self,request):
        """
        """
        SupersubManager()._delete_session_variables(request)
        context = {
            'main_form' : MainSearchForm(),
            'navbar_form' : NavbarSearchForm()
        }
        return render(request, 'supersub/index.html', context)


class ResutlView(View):
    """
    """
    def get(self, request):
        """
        """
        session_prod_id, session_prods_ids = SupersubManager()._get_session_variables(request)
        if session_prods_ids:
            context = SupersubManager()._get_context_from_session_variables(request, session_prod_id, session_prods_ids)
            return render(request, 'supersub/results.html', context)
        else:
            if request.method == 'GET':
                # form = SearchForm(request.GET)
                main_form = MainSearchForm(request.GET)
                nav_form = NavbarSearchForm(request.GET)
                if main_form:
                    form = main_form
                elif nav_form:
                    form = nav_form
                if form.is_valid():
                    matching_products = Product.objects.filter(name__contains=form.cleaned_data['searched_string'])[:1]
                    if matching_products:
                        context = SupersubManager()._get_context_from_form(request, matching_products) 
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
                .select_related('product').order_by('id'))
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


class LegalMentionsView(View):
    """
    """
    def get(self,request):
        """
        """
        return render(request, 'supersub/legal_mentions.html')
