from django.template.loader import render_to_string
from django.test import TestCase


class IndexViewTest(TestCase):
    """
    """
    def test_index_template_is_true(self):
        response = self.client.get('/supersub/')
        self.assertTemplateUsed(response, 'supersub/index.html')