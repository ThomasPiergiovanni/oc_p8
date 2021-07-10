# pylint: disable=W0212
""" Favorites view module.
"""
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from supersub.views.custom_view import CustomView


class FavoritesView(CustomView):
    """Favorites view class.
    """
    def __init__(self):
        super().__init__()
        self.data['render'] = 'supersub/favorites.html'
        self.data['redirect'] = 'supersub:index'

    def get(self, request):
        """ Favorite view method on client get request. The response renders
        all the favorites from the authenticated user. In case the user has
        not register any favorite or he'll be redirected ot the index page.
        The same will occur if an un-auntehnticated user try ot see its
        favorites.
        """
        if request.user.is_authenticated:
            favorites = list(self.manager._filter_favorites(request.user.id))
            if favorites:
                self.data['ctxt']['page_obj'] = (
                    self.manager._get_page(request, favorites)
                )
                return render(
                    request, self.data['render'], self.data['ctxt'])
            messages.add_message(
                request,
                messages.WARNING,
                "Vous n'avez enregistré aucun favoris jusqu'à présent"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Connectez-vous pour consulter vos favoris!"
            )
        return HttpResponseRedirect(reverse(self.data['redirect']))
