from django.test import TestCase

from supersub.forms import NavbarSearchForm


class LegalMentionsViewTest(TestCase):
    """
    """
    def test_get_with_status_code_200(self):
        response = self.client.get('/supersub/legal_mentions/')
        self.assertEqual(response.status_code, 200)

    def test_get_with_template(self):
        response = self.client.get('/supersub/legal_mentions/')
        self.assertTemplateUsed(response, 'supersub/legal_mentions.html')
    
    def test_get_with_navbar_form(self):
        response = self.client.get('/supersub/legal_mentions/')
        self.assertIsInstance(response.context['navbar_form'], NavbarSearchForm)