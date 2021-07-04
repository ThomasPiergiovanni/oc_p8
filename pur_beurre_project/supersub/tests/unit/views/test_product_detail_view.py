from django.test import TestCase

from supersub.forms.navbar_search_form import NavbarSearchForm
from supersub.models.product import Product
from supersub.tests.integration.models.test_category import CategoryTest
from supersub.tests.integration.models.test_product import ProductTest


class ProductDetailViewTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        CategoryTest().emulate_category()
        ProductTest().emulate_product()
    
    def setUp(self):
        self.response = self.client.get('/supersub/product_detail/1')

    def test_get_with_status_code_200(self):
        self.assertEquals(self.response.status_code, 200)

    def test_get_with_template(self):
        self.assertTemplateUsed(self.response, 'supersub/product_detail.html')
    
    def test_get_with_navbar_form(self):
        self.assertIsInstance(
            self.response.context['navbar_form'],
            NavbarSearchForm 
        )
    
    def test_get_with_product(self):
        product = Product.objects.get(pk=1)
        self.assertEquals(self.response.context['prod'], product)