from django.test import TestCase

from supersub.models.product import Product
from supersub.tests.unit.models.test_category import CategoryTest
from supersub.tests.unit.models.test_product import ProductTest



class ResultViewTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        CategoryTest.emulate_category()
        ProductTest.emulate_product() 

    def test_post_with_response_200(self):
        response = self.client.post(
            '/supersub/results/',
            data={'product':'Product_for_test'})
        self.assertEqual(response.status_code,200)
    
    def test_post_with_product(self):
        response = self.client.post(
            '/supersub/results/',
            data={'product':'Product_for_test'})
        product = Product.objects.get(pk=1)
        self.assertEqual(response.context['searched_prod'], product)
    
    def test_post_with_page_objects(self):
        response = self.client.post(
            '/supersub/results/',
            data={'product':'Product_for_test'})
        self.assertEquals(response.context['page_obj'][0].id, 2)
        self.assertEquals(response.context['page_obj'][1].id, 3)

