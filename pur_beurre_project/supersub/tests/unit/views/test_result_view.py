from django.test import TestCase

from supersub.forms.navbar_search_form import NavbarSearchForm
from supersub.tests.integration.models.test_category import CategoryTest
from supersub.tests.integration.models.test_product import ProductTest



class ResultViewTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        CategoryTest.emulate_category()
        ProductTest.emulate_product()
    
    def setUp(self):
        self.session = None

    def test_get_with_response_200(self):
        self.emulate_session()
        self.response = self.client.get('/supersub/results/')
        self.assertEqual(self.response.status_code,200)
    
    def emulate_session(self):
        session = self.client.session
        session['prod_id'] = 1
        session['prods_ids'] = [2,3]
        session.save()
    
    def test_get_with_page_products(self):
        self.emulate_session()
        response = self.client.get('/supersub/results/')
        self.assertEquals(response.context['page_obj'][0].id, 2)
        self.assertEquals(response.context['page_obj'][1].id, 3)
    
    def test_get_with_render(self):
        self.emulate_session()
        response = self.client.get('/supersub/results/')
        self.assertTemplateUsed(response, 'supersub/results.html')
    
    def test_get_with_navbar_form(self):
        self.emulate_session()
        response = self.client.get('/supersub/results/')
        self.assertIsInstance(response.context['navbar_form'], NavbarSearchForm)

    def test_post_with_response_200(self):
        response = self.client.post(
            '/supersub/results/',
            data={'product':'Pain 100% mie nature PT - Harrys - 500 g'})
        self.assertEqual(response.status_code,200)
    
    def test_post_with_product(self):
        response = self.client.post(
            '/supersub/results/',
            data={'product':'Pain'})
        self.assertEqual(response.context['searched_prod'].id, 1)
    
    def test_post_with_page_products(self):
        response = self.client.post(
            '/supersub/results/',
            data={'product':'Pain'})
        self.assertEquals(response.context['page_obj'][0].id, 2)
    
    def test_post_with_warning_message(self):
        response = self.client.post(
            '/supersub/results/',
            data={'product':"ZzzzZ"}, follow=True)
        for message in response.context['messages']:
            self.assertEqual(message.level_tag, 'warning')
            self.assertEqual(
                message.message,
                "Ce produit n'a pas été reconnu ou n'existe pas.")
    
    def test_post_with_error_message(self):
        response = self.client.post(
            '/supersub/results/',
            data={'product': ""}, follow=True)
        for message in response.context['messages']:
            self.assertEqual(message.level_tag, 'error')
            self.assertEqual(message.message, "Saisissez un produit")
    
    def test_post_with_redirect(self):
        response = self.client.post(
            '/supersub/results/',
            data={'product': ""}, follow=True)
        self.assertEquals(response.redirect_chain[0][0], '/supersub/')
    
    def test_post_with_navbar_form(self):
        response = self.client.post(
            '/supersub/results/',
            data={'product':"ZzzzZ"}, follow=True)
        self.assertIsInstance(response.context['navbar_form'], NavbarSearchForm)


