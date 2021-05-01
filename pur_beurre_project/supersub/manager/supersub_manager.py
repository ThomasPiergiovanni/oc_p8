from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from supersub.models import Favorites, Product
from supersub.forms import MainSearchForm, NavbarSearchForm


class SupersubManager():
    """
    """
    def _get_context_from_session_variables(
            self, request, session_prod_id, session_prods_ids):
        """
        """
        products_candidates = (
            self._get_results_products(session_prods_ids))
        context = {
            'searched_product': self._get_product(session_prod_id),
            'page_object' : self._paginate(request, products_candidates)
        }
        return context
    
    def _get_results_products(self, session_prods_ids):
        """
        """
        products_candidates = []
        for session_fav_cand_id in session_prods_ids:
            products_candidates.append(self._get_product(session_fav_cand_id))
        return products_candidates
    
    def _get_product(self, id_product):
        """
        """
        return Product.objects.get(pk=id_product)
    
    def _get_forms(self, request):
        """
        """
        main_form = MainSearchForm(request.GET)
        nav_form = NavbarSearchForm(request.GET)
        if main_form:
            return main_form
        elif nav_form:
            return nav_form

    
    def _get_searched_string(self,request):
        """
        """
        return request.GET.get('product', None)
  
    def _get_context_from_form(self, request, matching_products):
        """
        """
        product = matching_products[0]
        products_candidates = self._get_products_candidates(product)
        session_prods_ids = (
            self._get_session_prods_ids(products_candidates))
        self._add_variables_to_session(
            request, product.id, session_prods_ids)
        context = {
            'searched_product': product,
            'page_object' : self._paginate(request, products_candidates)
        }
        return context
    
    def _get_products_candidates(self, product):
        """
        """
        return (
            Product.objects.filter(category_id=product.category_id)
            .filter(nutriscore_grade__lte=product.nutriscore_grade)
            .exclude(id__exact=product.id).order_by('id'))
    
    def _get_session_prods_ids(self, products_candidates):
        """
        """
        session_prods_ids =[]
        for candidate in products_candidates:
            session_prods_ids.append(candidate.id)
        return session_prods_ids

    def _add_variables_to_session(
            self, request, session_prod_id, session_prods_ids):
        """
        """
        request.session['session_prod_id'] = session_prod_id
        request.session['session_prods_ids'] = session_prods_ids

    def _paginate(self, request, objects_list):
        """
        """
        paginator = Paginator(objects_list, 6)
        page_number = request.GET.get ('page')
        return paginator.get_page(page_number)

    
    def _delete_session_variables(self, request):
        """
        """
        _session_prod_id, session_prods_ids = self._get_session_variables(request)
        if _session_prod_id and session_prods_ids:
            del request.session['session_prod_id']
            del request.session['session_prods_ids']

    def _get_session_variables(self, request):
        """
        """
        session_prod_id = request.session.get('session_prod_id', None)
        session_prods_ids = request.session.get('session_prods_ids', None)
        return session_prod_id, session_prods_ids
   
    def _get_favorite(self, id_product, id_user):
        """
        """
        try: 
            return Favorites.objects.get(product_id__exact=id_product, custom_user_id__exact=id_user)
        except:
            return None
