from django.test import TestCase

# from supersub.models import Category, Product

from supersub.models.product import Product
from supersub.models.category import Category


class ResultViewTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        cls.emulate_category()
        cls.emulate_product()
    
    @classmethod
    def emulate_category(cls):
        Category.objects.create(
            id=1,
            name="CategorieOne",
            url="www.categorie_test.com")
    
    @classmethod
    def emulate_product(cls):
        Product.objects.create(
            id=1,
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

    def test_index_page_POST_request_with_response_200(self):
        response = self.client.post('/supersub/results/',data={'product':'Product_for_test'})
        self.assertEqual(response.status_code,200)
    
    def test_index_page_POST_request_with_context_correct(self):
        response = self.client.post('/supersub/results/',data={'product':'Product_for_test'})
        product = Product.objects.get(pk=1)
        self.assertEqual(response.context['searched_prod'], product)