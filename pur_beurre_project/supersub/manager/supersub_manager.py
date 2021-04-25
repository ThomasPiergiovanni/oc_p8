from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, redirect
from supersub.models import Favorites


class SupersubManager():
    """
    """
    def __init__(self):
        self.product_id = None
        self.candidates_favorites_ids = None

    def _add_variables_to_session(
            self, request, product_id, candidates_favorites_ids):
        """
        """
        request.session['product_id'] = product_id
        request.session['candidates_favorites_ids'] = candidates_favorites_ids
    
    def _delete_session_variables(self, request):
        self._get_session_variables(request)
        if self.product_id and self.candidates_favorites_ids:
            del request.session['product_id']
            del request.session['candidates_favorites_ids']

    def _get_session_variables(self, request):
        """
        """
        self.product_id = request.session.get('product_id', None)
        self.candidates_favorites_ids = request.session.get('candidates_favorites_ids', None)

    def _paginate(self, request, objects_list):
        """
        """
        paginator = Paginator(objects_list, 6)
        page_number = request.GET.get ('page')
        page_object = paginator.get_page(page_number)
        return page_object
     
    def _get_favorite(self, id_product, id_user):
        """
        """
        try: 
            return Favorites.objects.get(product_id__exact=id_product, custom_user_id__exact=id_user)
        except:
            return None
