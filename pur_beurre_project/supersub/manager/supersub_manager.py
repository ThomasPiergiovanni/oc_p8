from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from supersub.models import Favorites, Product


class SupersubManager():
    """
    """
    def __init__(self):
        self.session_prod_id = None
        self.session_favs_cands_ids = None
    
    def _display_results_from_session_variables(self, request, session_prods_id, session_favs_cands_ids):
        """
        """
        favorites_candidates = (
            self._create_favorites_candidates(session_favs_cands_ids))
        product = Product.objects.get(pk=session_prods_id)
        context = {
            'searched_product': product,
            'page_object' : self._paginate(request, favorites_candidates)
        }
        return context
    
    def _create_favorites_candidates(self, session_favs_cands_ids):
        """
        """
        favorites_candidates = []
        for favorite_candidate_id in session_favs_cands_ids:
            product = Product.objects.get(pk=favorite_candidate_id)
            favorites_candidates.append(product)
        return favorites_candidates
    
    def _get_session_favs_cands_ids(self, favorites_candidates):
        """
        """
        session_favs_cands_ids =[]
        for candidate in favorites_candidates:
            session_favs_cands_ids.append(candidate.id)
        return session_favs_cands_ids

    def _add_variables_to_session(
            self, request, session_prod_id, session_favs_cands_ids):
        """
        """
        request.session['session_prod_id'] = session_prod_id
        request.session['session_favs_cands_ids'] = session_favs_cands_ids
    
    def _delete_session_variables(self, request):
        self._get_session_variables(request)
        if self.session_prod_id and self.session_favs_cands_ids:
            del request.session['session_prod_id']
            del request.session['session_favs_cands_ids']

    def _get_session_variables(self, request):
        """
        """
        self.session_prod_id = request.session.get('session_prod_id', None)
        self.session_favs_cands_ids = request.session.get('session_favs_cands_ids', None)

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
