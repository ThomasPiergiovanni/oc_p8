from django.test import TestCase

from supersub.forms import MainSearchForm, NavbarSearchForm


class IndexViewTest(TestCase):
    """
    """
    def test_index_page_GET_request(self):
        response = self.client.get('/supersub/')
        self.assertEqual(response.status_code, 200)

    def test_index_page_template_is_true(self):
        response = self.client.get('/supersub/')
        self.assertTemplateUsed(response, 'supersub/index.html')
    
    def test_index_page_uses_main_form(self):
        response = self.client.get('/supersub/')
        self.assertIsInstance(response.context['main_form'], MainSearchForm)
    
    def test_index_page_uses_navbar_form(self):
        response = self.client.get('/supersub/')
        self.assertIsInstance(response.context['navbar_form'], NavbarSearchForm)