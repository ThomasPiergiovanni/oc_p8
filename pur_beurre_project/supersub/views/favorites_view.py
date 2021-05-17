from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from supersub.models.favorites import Favorites
from supersub.views.custom_view import CustomView


class FavoritesView(CustomView):
    """
    """
    def __init__(self):
        """
        """
        super().__init__()
        self.data['render'] = 'supersub/favorites.html'
        self.data['redirect'] = 'supersub:index'

    def get(self, request):
        if request.user.is_authenticated:
            favorites = list(
                Favorites.objects
                .filter(custom_user_id__exact=request.user.id)
                .select_related('product').order_by('id'))
            if favorites:
                self.data['ctxt']['page_obj'] = (
                    self.manager._get_page(request, favorites))
                return render(
                    request, self.data['render'], self.data['ctxt'])
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