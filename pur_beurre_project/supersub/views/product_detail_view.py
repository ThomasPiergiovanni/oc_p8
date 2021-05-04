from django.shortcuts import render

from supersub.forms import NavbarSearchForm
from supersub.views.custom_view import CustomView


class ProductDetailView(CustomView):
    """
    """
    def __init__(self):
        """
        """
        super().__init__()
        self.data['render'] = 'supersub/product_detail.html'
        
    def get(self, request, id_prod):
        """
        """
        self.data['ctxt']['prod'] = self.manager._get_product(id_prod)
        return render(request, self.data['render'], self.data['ctxt'])