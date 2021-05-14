from django.core.paginator import Paginator
from django.test import TestCase, RequestFactory
from supersub.manager.supersub_manager import SupersubManager
from supersub.models import Category, Product

# Create your tests here.

class SupersubManagerTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        cls.emulate_data()
        cls.emulate_category()
        cls.emulate_product()
        cls.prod1 = Product.objects.get(pk=1)
        cls.prod2 = Product.objects.get(pk=2)
        cls.prods_list = cls.emulate_prods_list(cls.prod1, cls.prod2)
        cls.prods_ids = cls.emulate_prods_ids_list(cls.prod1, cls.prod2)
        cls.request_GET = RequestFactory().get('', data={'page':1})
        cls.request_POST = RequestFactory().post('', data={'product':cls.prod1})
        cls.paginator = Paginator(cls.prods_list, 6)
    
    @classmethod
    def emulate_data(cls):
        cls.data = {
            'ctxt': {},
            'render':"",
            'redirect':""
        }

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
        Product.objects.create(
            id=2,
            id_origin = 'kmihnl',
            name = 'Product_for_test2',
            nutriscore_grade = 'B',
            fat = 94.56,
            saturated_fat = 95.56,
            sugar=96.56,
            salt=97.56,
            image='www.imageurlbidon2.com',
            url='www.urlbidon.com',
            categories='cat1, cat2, cat3',
            category_id=1
        )
    
    @classmethod
    def emulate_prods_list(cls, prod_one, prod_two):
        """
        """
        prods = []
        prods.append(prod_one)
        prods.append(prod_two)
        return prods
    
    @classmethod
    def emulate_prods_ids_list(cls, prod_one, prod_two):
        prods_ids =[]
        prods_ids.append(prod_one.id)
        prods_ids.append(prod_two.id)
        return prods_ids

    def test__get_data(self):
        data = SupersubManager()._get_data()
        self.assertEqual(data, self.data)

    def test__get_page_from_session_vars_with_prod_name(self):
        page = SupersubManager()._get_page_from_session_vars(
            self.request_GET, self.prods_ids)
        prod_name = self.get_page_product_name(page)
        self.assertEqual(prod_name, 'Product_for_test')
    
    def get_page_product_name(self, page):
        for product in page:
            if product.id == 1:
                return product.name

    def test__get_results_prods_with_prods_list(self):
        """
        """
        products = SupersubManager()._get_results_prods(self.prods_ids)
        self.assertEqual(products, self.prods_list)
    
    def test__get_product_with_product(self):
        product = SupersubManager()._get_product(self.prod1.id)
        self.assertEqual(product, self.prod1)
    
    def test__get_page_with_prod_name(self):
        page = SupersubManager()._get_page(self.request_GET, self.prods_list)
        self.assertEqual(self.get_page_product_name(page),'Product_for_test')
    
    def test__get_paginator_with_num_pages(self):
        paginator = SupersubManager()._get_paginator(self.prods_list)
        self.assertEqual(paginator.num_pages, self.paginator.num_pages)

    def test__get_paginator_with_prod_name(self):
        paginator = SupersubManager()._get_paginator(self.prods_list)
        self.assertEqual(
            self.get_paginator_product_name(paginator),
            self.get_paginator_product_name(self.paginator))

    def get_paginator_product_name(self, paginator):
        for page in paginator:
            if page.number == 1:
                product = page.object_list[0]
                return product.name
    
    def test__request_page_number_with_page_number(self):
        page_number = SupersubManager()._get_request_page_number(self.request_GET)
        self.assertEqual(page_number, '1')
    
    def test__get_form_with_form(self):
        form =  SupersubManager()._get_form_value(self.request_POST)
        self.assertTrue(form)
