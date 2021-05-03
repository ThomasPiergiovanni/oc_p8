from django.views import View
from django.shortcuts import render

from supersub.forms import NavbarSearchForm
from supersub.manager.supersub_manager import SupersubManager

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