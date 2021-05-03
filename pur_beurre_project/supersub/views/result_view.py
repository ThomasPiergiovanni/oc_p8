from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from supersub.models import Product
from supersub.forms import NavbarSearchForm
from supersub.manager.supersub_manager import SupersubManager
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
                messages.ERROR,"Saisissez un produit")
        return HttpResponseRedirect(reverse(self.data['redirect']))