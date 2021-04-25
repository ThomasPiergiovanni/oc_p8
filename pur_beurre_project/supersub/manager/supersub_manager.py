from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from supersub.models import Favorites, Product


class SupersubManager():
    """
    """
    def __init__(self):
        self.product_id = None
        self.favorites_candidates_ids = None
    
    def _create_favorites_candidates(self, favorites_candidates_ids):
        """
        """
        favorites_candidates = []
        for favorite_candidate_id in favorites_candidates_ids:
            product = Product.objects.get(pk=favorite_candidate_id)
            favorites_candidates.append(product)
        return favorites_candidates
    
    def _get_favorites_candidates_ids(self, favorites_candidates):
        """
        """
        favorites_candidates_ids =[]
        for candidate in favorites_candidates:
            favorites_candidates_ids.append(candidate.id)
        return favorites_candidates_ids

    def _add_variables_to_session(
            self, request, product_id, favorites_candidates_ids):
        """
        """
        request.session['product_id'] = product_id
        request.session['favorites_candidates_ids'] = favorites_candidates_ids
    
    def _delete_session_variables(self, request):
        self._get_session_variables(request)
        if self.product_id and self.favorites_candidates_ids:
            del request.session['product_id']
            del request.session['favorites_candidates_ids']

    def _get_session_variables(self, request):
        """
        """
        self.product_id = request.session.get('product_id', None)
        self.favorites_candidates_ids = request.session.get('favorites_candidates_ids', None)

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
