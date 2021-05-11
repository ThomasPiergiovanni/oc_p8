from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):
    """
    """
    def test_index_GET_request(self):
        response = self.client.get('/supersub/')
        self.assertEqual(response.status_code, 200)

    def test_index_template_is_true(self):
        response = self.client.get('/supersub/')
        self.assertTemplateUsed(response, 'supersub/index.html')


class ResultViewTest(TestCase):
    """
    """
    def test_index_form_POST_request(self):
        response = self.client.post('/supersub/',data={'product': "Nutella"})
        self.assertIn("Nutella", response.content.decode())
