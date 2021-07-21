# pylint: disable=C0116
"""Test legal mention view module.
"""
from django.test import TestCase

from supersub.forms.navbar_search_form import NavbarSearchForm


class LegalMentionsViewTest(TestCase):
    """Test legal mention view class.
    """
    def setUp(self):
        self.response = self.client.get('/legal_mentions/')

    def test_get_with_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_get_with_template(self):
        self.assertTemplateUsed(self.response, 'supersub/legal_mentions.html')

    def test_get_with_navbar_form(self):
        self.assertIsInstance(
            self.response.context['navbar_form'],
            NavbarSearchForm
        )
