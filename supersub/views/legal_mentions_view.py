# pylint: disable=W0212
"""Legal mentions view module.
"""
from django.shortcuts import render

from supersub.views.custom_view import CustomView


class LegalMentionsView(CustomView):
    """Legal mentions view class.
    """
    def __init__(self):
        super().__init__()
        self._data['render'] = 'supersub/legal_mentions.html'

    def get(self, request):
        """Legal mention page view method on client get request.
        """
        return render(request, self._data['render'], self._data['ctxt'])
