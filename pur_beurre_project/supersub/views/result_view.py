from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from supersub.models.product import Product
from supersub.views.custom_view import CustomView


class ResultView(CustomView):
    """
    """
    def __init__(self):
        """
        """
        super().__init__()
        self.data['render'] = 'supersub/results.html'
        self.data['redirect'] = 'supersub:index'

    def get(self, request):
        """
        """
        prod_id, prods_ids = self.manager._get_session_vars(request)
        self.data['ctxt']['searched_prod'] = self.manager._get_product(prod_id)
        self.data['ctxt']["page_obj"] = (
            self.manager._get_page_from_session_vars(request, prods_ids))
        return render(request, self.data['render'], self.data['ctxt'])


    def post(self, request):
        """
        """
        form = self.manager._get_form(request)
        if form.is_valid():
            match_prods = (
                Product.objects.filter(
                name__contains=form.cleaned_data['product'])[:1])
            if match_prods:
                self.data['ctxt']['searched_prod'] = match_prods[0]
                self.data['ctxt']["page_obj"] = (
                    self.manager._get_page_from_form(request, match_prods[0]))
                self.manager._add_vars_to_session(request, match_prods[0])
                self.data['ctxt']['user'] = request.user
                return render(
                    request, self.data['render'], self.data['ctxt'])
            else:
                messages.add_message(
                    request,
                    messages.WARNING,
                    "Ce produit n'a pas été reconnu ou n'existe pas.")
        else:
            messages.add_message(
                request,
                messages.ERROR,"Saisissez un produit")
        return HttpResponseRedirect(reverse(self.data['redirect']))