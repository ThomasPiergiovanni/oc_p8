from django.core.paginator import Paginator
from django.test import TestCase, RequestFactory

from authentication.models import CustomUser
from supersub.forms import MainSearchForm, NavbarSearchForm
from supersub.manager.supersub_manager import SupersubManager

from supersub.models.favorites import Favorites
from supersub.models.product import Product
from supersub.tests.unit.models.test_category import CategoryTest
from supersub.tests.unit.models.test_product import ProductTest



# Create your tests here.

class SupersubManagerTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        cls.emulate_data()
        CategoryTest.emulate_category()
        ProductTest.emulate_product()
        cls.prod1 = Product.objects.get(pk=1)
        cls.prod2 = Product.objects.get(pk=2)
        cls.prod3 = Product.objects.get(pk=3)
        cls.prods_list = cls.emulate_prods_list(cls.prod1, cls.prod2)
        cls.prods_ids = cls.emulate_prods_ids_list(cls.prod1, cls.prod2)
        cls.request_GET = RequestFactory().get('', data={'page':1})
        cls.request_POST = RequestFactory().post('', data={'page':1, 'product':cls.prod1.name})
        cls.paginator = Paginator(cls.prods_list, 6)
        cls.emulate_favorites()
        cls.emulate_custom_user()
        cls.custom_user = CustomUser.objects.get(pk=1)
    
    @classmethod
    def emulate_data(cls):
        cls.data = {
            'ctxt': {},
            'render':"",
            'redirect':""
        }  
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
       
    @classmethod
    def emulate_custom_user(cls):
        custom_user = CustomUser.objects.create_user(
                id=1,
                email='testuser@email.com',
                password='_Xxxxxxx',
                first_name='tester')
    
    @classmethod
    def emulate_favorites(cls):
        Favorites.objects.create(product_id=1, custom_user_id=1)

    def test__get_data(self):
        data = SupersubManager()._get_data()
        self.assertEqual(data, self.data)

    def test__get_page_from_session_vars_with_prod_name(self):
        page = SupersubManager()._get_page_from_session_vars(
            self.request_GET, self.prods_ids)
        self.assertEqual(page[0].name, 'Product_for_test')

    def test__get_results_prods_with_prods_list(self):
        products = SupersubManager()._get_results_prods(self.prods_ids)
        self.assertEqual(products, self.prods_list)
    
    def test__get_product_with_product(self):
        product = SupersubManager()._get_product(self.prod1.id)
        self.assertEqual(product, self.prod1)
    
    def test__get_page_with_prod_name(self):
        page = SupersubManager()._get_page(self.request_GET, self.prods_list)
        self.assertEqual(page[0].name,'Product_for_test')
    
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
        form =  SupersubManager()._get_form(self.request_POST)
        self.assertTrue(
            type(form),
            type(MainSearchForm()) or type(NavbarSearchForm()))
    
    def test__get_page_from_form_with_prod_name(self):
        page = SupersubManager()._get_page_from_form(
            self.request_POST, self.prod1)
        self.assertEqual(page[0].name,'Product_for_test2')
        self.assertEqual(page[1].name,'Product_for_test3')
    
    def test__get_session_prods_with_prod_id(self):
        prods = SupersubManager()._get_session_prods(self.prod1)
        self.assertEqual(prods[0].id, 2)
        self.assertEqual(prods[1].id, 3)
    
    def test__get_session_prods_ids_with_prods_list(self):
        prods_ids = SupersubManager()._get_session_prods_ids(self.prods_list)
        self.assertEqual(prods_ids, self.prods_ids)
    
    def test__add_vars_to_session_with_prod_id_and_prods_ids(self):
        setattr(self.request_POST, 'session', {'prod_id':'', 'prods_ids':''})
        SupersubManager()._add_vars_to_session(self.request_POST, self.prod1)
        self.assertEqual(self.request_POST.session['prod_id'], 1)
        self.assertEqual(self.request_POST.session['prods_ids'], [2, 3])
    
    def test__delete_session_vars_with_none(self):
        setattr(self.request_GET, 'session', {
            'prod_id': 1, 'prods_ids': [2, 3]})
        SupersubManager()._delete_session_vars(self.request_GET)
        self.assertEqual(
            self.request_GET.session.get('prod_id', None), None)
        self.assertEqual(
            self.request_GET.session.get('prods_ids', None), None)
    
    def test__get_session_vars_with_prod_id_and_prods_ids(self):
        setattr(
            self.request_GET, 'session', {'prod_id': 1,'prods_ids': [2, 3]})
        prod_id, prods_ids = (
            SupersubManager()._get_session_vars(self.request_GET))
        self.assertEqual(prod_id, 1)
        self.assertEqual(prods_ids, [2, 3])
    
    def test__get_favorite_with_class_type_is_true(self):
        favorites = SupersubManager()._get_favorite(1, 1)
        self.assertTrue(favorites, type(Favorites()))
    
    def test__get_favorite_with_class_type_is_none(self):
        favorites = SupersubManager()._get_favorite(1, 2)
        self.assertFalse(favorites, type(Favorites()))
    
