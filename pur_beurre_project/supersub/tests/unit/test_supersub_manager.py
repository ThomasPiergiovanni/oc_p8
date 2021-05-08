from django.test import TestCase
from supersub.manager.supersub_manager import SupersubManager
from supersub.models import Category, Product

# Create your tests here.

class SupersubManagerTest(TestCase):
    """
    """
    def setUp(self):
        self.data = self.emulate_data
        self.category = self.emulate_category

    def test__get_data(self):
        """
        """
        data = SupersubManager()._get_data()
        self.assertEqual(data, self.data)
    
    @property
    def emulate_data(self):
        data = {
            'ctxt': {},
            'render':"",
            'redirect':""
        }
        return data
    
    def test__get_results_prods(self):
        """
        """
        self.category
        prod_one =self.emulate_product(name="Prod One", category=self.category)
        prod_two =self.emulate_product(name="Prod Two", category=self.category)
        prods = self.emulate_prods_list(prod_one=prod_one, prod_two=prod_two)
        prods_ids =self.emulate_prods_ids_list(prod_one, prod_two)
        products = SupersubManager()._get_results_prods(prods_ids)
        self.assertEqual(products, prods)

    @property
    def emulate_category(self):
        category = Category.objects.create(
            name="Categorie",
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
        prod = self.emulate_product(name="Produit", category=self.category)
        product = SupersubManager()._get_product(prod.id)
        self.assertEqual(product, prod )
