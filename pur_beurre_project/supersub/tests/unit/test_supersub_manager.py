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
        Product.objects.create(
            id=2,
            id_origin = 'koikik',
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

    def setUp(self):
        self.data = self.emulate_data()
        # self.category = self.emulate_category("CatOne")
        # self.prod_one = self.emulate_product("ProdOne", self.category)
        # self.prod_two = self.emulate_product("ProdTwo", self.category)
        product = Product.objects.get(pk=1)
        product2 = Product.objects.get(pk=2)
        self.prods_list = self.emulate_prods_list(
            product, product2)
        # self.prods_ids = self.emulate_prods_ids_list(
        #     self.prod_one, self.prod_two)
        self.prods_ids = self.emulate_prods_ids_list(product,product2)
        self.factory = RequestFactory()
    
    def emulate_data(self):
        data = {
            'ctxt': {},
            'render':"",
            'redirect':""
        }
        return data

    # def emulate_category(self, name):
    #     category = Category.objects.create(
    #         name=name,
    #         url="www.categorie_test.com")
    #     return category

    # def emulate_product(self, name, category):
    #     product = Product.objects.create(
    #         name=name,
    #         fat=110.56,
    #         saturated_fat=25.12,
    #         sugar=5.456,
    #         salt=2,
    #         category=category
    #     )
    #     return product

    def emulate_prods_list(self, prod_one, prod_two):
        """
        """
        prods = []
        prods.append(prod_one)
        prods.append(prod_two)
        return prods

    def emulate_prods_ids_list(self, prod_one, prod_two):
        """
        """
        prods_ids =[]
        prods_ids.append(prod_one.id)
        prods_ids.append(prod_two.id)
        return prods_ids
    
    def test__get_data(self):
        """
        """
        data = SupersubManager()._get_data()
        self.assertEqual(data, self.data)

    def test__get_from_session_vars(self):
        """
        """
        pass
    
    def test__get_results_prods(self):
        """
        """
        products = SupersubManager()._get_results_prods(self.prods_ids)
        self.assertEqual(products, self.prods_list)
        
    def test__get_page_with_page_num_one(self):
        request_test = self.factory.get('', data={'page':1})
        paginator_test = Paginator(self.prods_list, 6)
        page_test = paginator_test.get_page(1)
        page = SupersubManager()._get_page(request_test, self.prods_list)
        self.assertEqual(
            self._get_page_product_name(page),
            self._get_page_product_name(page_test))
    
    def _get_page_product_name_for_product_id_equal_1(self, page):
        for product in page:
            if product.id == 1:
                return product.name   
    
    def test__get_paginator_number_of_pages(self):
        paginator_test = Paginator(self.prods_list, 6)
        paginator =SupersubManager()._get_paginator(self.prods_list)
        self.assertEqual(paginator.num_pages, paginator_test.num_pages)

    def test__get_paginator_product_name_for_page_1_with_product_id_equal_1(self):
        paginator_test = Paginator(self.prods_list, 6)
        paginator = SupersubManager()._get_paginator(self.prods_list)
        self.assertEqual(
            self._get_product_name(paginator_test),
            self._get_product_name(paginator))

    def _get_product_name(self, objects_list):
        for page in objects_list:
            if page.number == 1:
                product = page.object_list[0]
                return product.name
    
    def test__request_page_number_with_page_equal_one(self):
        request_test = self.factory.get('', data={'page':1})
        page_number = SupersubManager()._get_request_page_number(request_test)
        self.assertEqual(page_number, '1')

    def test__get_product(self):
        """
        """
        # product = SupersubManager()._get_product(self.prod_one.id)
        # self.assertEqual(product, self.prod_one)
    
