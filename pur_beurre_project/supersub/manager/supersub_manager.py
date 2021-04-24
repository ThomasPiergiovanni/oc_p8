from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class SupersubManager():
    """
    """
    def add_variables_to_session(self,**kwargs):
        """
        """
        request = kwargs.get('request', None)
        product_id = kwargs.get('product_id', None)
        candidates_favorites_ids = kwargs.get('candidates_favorites_ids', None)
        if request:
            if product_id:
                request.session['product_id'] = product_id
            if candidates_favorites_ids:
                request.session['candidates_favorites_ids'] = candidates_favorites_ids

    def paginate(self, request, objects_list):
        """
        """
        paginator = Paginator(objects_list, 6)
        page_number = request.GET.get ('page')
        page_object = paginator.get_page(page_number)
        return page_object