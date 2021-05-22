from django.test import TestCase

from supersub.forms import MainSearchForm, NavbarSearchForm


class IndexViewTest(TestCase):
    """
    """
    def test_get_with_status_code_200(self):
        response = self.client.get('/supersub/')
        self.assertEqual(response.status_code, 200)

    def test_get_with_template(self):
        response = self.client.get('/supersub/')
        self.assertTemplateUsed(response, 'supersub/index.html')
    
    def test_index_with_main_form(self):
        response = self.client.get('/supersub/')
        self.assertIsInstance(response.context['main_form'], MainSearchForm)
    
    def test_index_with_navbar_form(self):
        response = self.client.get('/supersub/')
        self.assertIsInstance(response.context['navbar_form'], NavbarSearchForm)
