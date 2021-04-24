from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class SupersubManager():
    """
    """
    def paginate(self, request, objects_list):
        """
        """
        paginator = Paginator(objects_list, 6)
        page_number = request.GET.get ('page')
        page_object = paginator.get_page(page_number)
        return page_object