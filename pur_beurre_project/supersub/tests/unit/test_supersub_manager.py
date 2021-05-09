from django.test import TestCase
from supersub.manager.supersub_manager import SupersubManager
from supersub.models import Category, Product

# Create your tests here.

class SupersubManagerTest(TestCase):
    """
    """
    def setUp(self):
        self.data = self.emulate_data
        self.category = self.emulate_category("CatOne")
        self.prod_one = self.emulate_product("ProdOne", self.category)
        self.prod_two = self.emulate_product("ProdTwo", self.category)
    
    @property
    def emulate_data(self):
        data = {
            'ctxt': {},
            'render':"",
            'redirect':""
        }
        return data

    def emulate_category(self, name):
        category = Category.objects.create(
            name=name,
            url="www.categorie_test.com")
        return category

    def emulate_product(self, name, category):
        product = Product.objects.create(
            name=name,
            fat=110.56,
            saturated_fat=25.12,
            sugar=5.456,
            salt=2,
            category=category
        )
        return product
    
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
        prods = self.emulate_prods_list(self.prod_one, self.prod_two)
        prods_ids =self.emulate_prods_ids_list(self.prod_one, self.prod_two)
        products = SupersubManager()._get_results_prods(prods_ids)
        self.assertEqual(products, prods)
    
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

    def test__get_product(self):
        """
        """
        product = SupersubManager()._get_product(self.prod_one.id)
        self.assertEqual(product, self.prod_one)
    
    def test__paginate(self):
        pass
