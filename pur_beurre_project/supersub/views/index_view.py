# pylint: disable=W0212
"""Index view module.
"""
from django.shortcuts import render

from supersub.views.custom_view import CustomView


class IndexView(CustomView):
    """Index view class.
    """
    def __init__(self):
        super().__init__()
        self.data['render'] = 'supersub/index.html'

    def get(self, request):
        """Index/home page view method on client get request.
        """
        self._delete_session_vars(request)
        return render(request, self.data['render'], self.data['ctxt'])
