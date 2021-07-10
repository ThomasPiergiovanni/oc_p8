from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from supersub.models.favorites import Favorites
from supersub.views.custom_view import CustomView


class RegisterFavoriteView(CustomView):
    """
    """
    def __init__(self):
        """
        """
        super().__init__()
        self.data['redirect'] = 'supersub:product_detail'

    def get(self, request, id_prod):
        """
        """
        if self.manager._get_favorite(id_prod, request.user.id):
            messages.add_message(
                request, messages.WARNING,"Produit déja enregistré")
        else:
            self.manager._save_favorite(id_prod, request.user.id)
            messages.add_message(
                request, messages.SUCCESS,"Produit enregistré!")
        return HttpResponseRedirect(
            reverse(self.data['redirect'], args=[id_prod]))