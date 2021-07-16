# pylint: disable=W0212
"""Register favorite view module.
"""
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from supersub.views.custom_view import CustomView


class RegisterFavoriteView(CustomView):
    """Register favorite view class.
    """
    def __init__(self):
        super().__init__()
        self.data['redirect'] = 'supersub:product_detail'

    def get(self, request, id_prod):
        """Register favorite method on client get request. On the attempt
        of registering the favorite, the user is redirected to the product
        detail page. If the favorite is already a user favorites', he'll get
        a waring message. If the favorite is not already a user favorite, a
        success message is displayed.
        """
        if self._get_favorite(id_prod, request.user.id):
            messages.add_message(
                request, messages.WARNING, "Produit déja enregistré"
            )
        else:
            self._save_favorite(id_prod, request.user.id)
            messages.add_message(
                request, messages.SUCCESS, "Produit enregistré!"
            )
        return HttpResponseRedirect(
            reverse(self.data['redirect'], args=[id_prod])
        )
