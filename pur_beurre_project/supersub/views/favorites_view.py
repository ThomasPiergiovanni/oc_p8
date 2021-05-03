from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from supersub.models import Favorites
from supersub.forms import NavbarSearchForm
from supersub.manager.supersub_manager import SupersubManager

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