from django.shortcuts import render

from supersub.forms import NavbarSearchForm
from supersub.manager.supersub_manager import SupersubManager
from supersub.views.custom_view import CustomView


class ProductDetailView(CustomView):
    """
    """
    def __init__(self):
        """
        """
        super().__init__()
        self.data['render'] = 'supersub/product_detail.html'
        
    def get(self, request, id_product):
        """
        """
        self.data['context']['product'] = (
            SupersubManager()._get_product(id_product))
        return render(request, self.data['render'], self.data['context'])