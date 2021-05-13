from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import reverse

from supersub.forms import MainSearchForm, NavbarSearchForm
from supersub.models import Category, Product




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



class ResultViewTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(
            id=1,
            name="CategorieOne",
            url="www.categorie_test.com")
        Product.objects.create(
            id_origin = 'fevfvf',
            name = 'Product_for_test',
            nutriscore_grade = 'A',
            fat = 4.56,
            saturated_fat = 5.56,
            sugar=6.56,
            salt=7.56,
            image='www.imageurlbidon.com',
            url='www.urlbidon.com',
            categories='cat1, cat2, cat3',
            category_id=1
        )

    def test_index_page_POST_request(self):
        pass
        response = self.client.post('/supersub/results/',data={'product':'Product_for_test'})
        self.assertEqual(response.status_code,200)


