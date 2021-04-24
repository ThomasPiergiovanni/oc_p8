from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class SupersubManager():
    """
    """
    def __init__(self):
        self.request = None
        self.product_id = None
        self.candidates_favorites_ids = None

    def add_variables_to_session(self,**kwargs):
        """
        """
        self._get_session_variables(**kwargs)
        if self.request:
            if self.product_id:
                self.request.session['product_id'] = self.product_id
            if self.candidates_favorites_ids:
                self.request.session['candidates_favorites_ids'] = self.candidates_favorites_ids
    
    def _del_session_variables(self, **kwargs):
        pass

    
    def _get_session_variables(self, **kwargs):
        self.request = kwargs.get('request', None)
        self.product_id = kwargs.get('product_id', None)
        self.candidates_favorites_ids = kwargs.get('candidates_favorites_ids', None)

    def paginate(self, request, objects_list):
        """
        """
        paginator = Paginator(objects_list, 6)
        page_number = request.GET.get ('page')
        page_object = paginator.get_page(page_number)
        return page_object