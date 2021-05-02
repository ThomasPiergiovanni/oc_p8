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
    def __init__(self):
        """
        """
        self.data = SupersubManager()._get_data()
        self.data['context']['main_form'] = MainSearchForm()
        self.data['context']['navbar_form'] = NavbarSearchForm()
        self.data['render'] = 'supersub/index.html'

    def get(self,request):
        """
        """
        SupersubManager()._delete_session_variables(request)
        return render(request, self.data['render'], self.data['context'])


class ResutlView(View):
    """
    """
    def __init__(self):
        """
        """
        self.data = SupersubManager()._get_data()
        self.data['context']['navbar_form'] = NavbarSearchForm()
        self.data['render'] = 'supersub/results.html'
        self.data['redirect'] = 'supersub:index'

    def get(self, request):
        """
        """
        session_prod_id, session_prods_ids = (
            SupersubManager()._get_session_variables(request))
        self.data['context']['searched_product'] = (
            SupersubManager()._get_product(session_prod_id))
        self.data['context']["page_object"] = (
            SupersubManager()
            ._get_page_from_session_variables(request, session_prods_ids))
        return render(request, self.data['render'], self.data['context'])


    def post(self, request):
        """
        """
        form = SupersubManager()._get_form_value(request)
        if form.is_valid():
            matching_products = (
                Product.objects.filter(
                name__contains=form.cleaned_data['searched_string'])[:1])
            if matching_products:
                self.data['context']['searched_product'] = (
                    matching_products[0])
                self.data['context']["page_object"] = (
                    SupersubManager()
                    ._get_page_from_form(request, matching_products[0]))
                SupersubManager()._add_variables_to_session(
                    request, matching_products[0])
                return render(
                    request, self.data['render'], self.data['context'])
            else:
                messages.add_message(
                    request,
                    messages.WARNING,
                    "Ce produit n'a pas été reconnu ou n'existe pas.")
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Saisissez un produit")
        return HttpResponseRedirect(reverse(self.data['redirect']))


class ProductDetailView(View):
    """
    """
    def __init__(self):
        """
        """
        self.data = SupersubManager()._get_data()
        self.data['context']['navbar_form'] = NavbarSearchForm()
        self.data['context']['product'] = ""
        self.data['render'] = 'supersub/product_detail.html'
        
    def get(self, request, id_product):
        """
        """
        self.data['context']['product'] = (
            SupersubManager()._get_product(id_product))
        return render(request, self.data['render'], self.data['context'])


class FavoritesView(View):
    """
    """
    def __init__(self):
        """
        """
        self.data = SupersubManager()._get_data()
        self.data['context']['navbar_form'] = NavbarSearchForm()
        self.data['render'] = 'supersub/favorites.html'
        self.data['redirect'] = 'supersub:index'

    def get(self, request):
        if request.user.is_authenticated:
            favorites = list(
                Favorites.objects
                .filter(custom_user_id__exact=request.user.id)
                .select_related('product').order_by('id'))
            if favorites:
                self.data['context']['page_object'] = (
                    SupersubManager()._paginate(request, favorites))
                return render(
                    request, self.data['render'], self.data['context'])
            else:
                messages.add_message(
                    request,
                    messages.WARNING,
                    "Vous n'avez enregistré aucun favoris jusqu'à présent")
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Connectez-vous pour consulter vos favoris!")
        return HttpResponseRedirect(reverse(self.data['redirect']))


class RegisterFavoriteView(View):
    """
    """
    def get(self, request, id_product):
        """
        """
        if SupersubManager()._get_favorite(id_product, request.user.id):
            messages.add_message(
                request, messages.WARNING,"Produit déja enregistré")
        else:
            Favorites(
                product_id=id_product,
                custom_user_id=request.user.id).save()
            messages.add_message(
                request,
                messages.SUCCESS,"Produit enregistré!")
        return HttpResponseRedirect(
            reverse('supersub:product_detail', args=[id_product]))


class LegalMentionsView(View):
    """
    """
    def __init__(self):
        """
        """
        self.data = SupersubManager()._get_data()
        self.data['context']['navbar_form'] = NavbarSearchForm()
        self.data['render'] = 'supersub/legal_mentions.html'

    def get(self,request):
        """
        """
        return render(request, self.data['render'], self.data['context'] )
