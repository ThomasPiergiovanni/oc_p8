from django.test import TestCase

from supersub.models.product import Product
from supersub.tests.unit.models.test_category import CategoryTest


class ProductTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        CategoryTest().emulate_category()
        cls.emulate_product()
    
    @classmethod
    def emulate_product(cls):
        Product.objects.create(
            id=1,
            id_origin = 'fevfvf',
            name = 'Pain 100% mie nature PT - Harrys - 500 g',
            nutriscore_grade = 'B',
            fat = 4.3,
            saturated_fat = 0.4,
            sugar= 7.7,
            salt= 1.13,
            image='https://static.openfoodfacts.org/images/products/322/885/'\
                '700/0852/front_fr.134.400.jpg',
            url='https://fr.openfoodfacts.org/produit/3228857000852/'\
                'pain-100-mie-nature-pt-harrys',
            categories='Aliments et boissons à base de végétaux,'\
                'Aliments d\'origine végétale, Céréales et pommes de terre,'\
                'Pains, Pains de mie, Pains de mie sans croûte',
            category_id=1
        )
        Product.objects.create(
            id=2,
            id_origin = 'kmihnl',
            name = 'Wasa tartine croustillante fibres - 230 g',
            nutriscore_grade = 'A',
            fat = 5,
            saturated_fat = 1,
            sugar= 2,
            salt= 1.1,
            image='https://static.openfoodfacts.org/images/products/730/'\
                '040/048/1588/front_fr.142.400.jpg',
            url='https://fr.openfoodfacts.org/produit/7300400481588/'\
                'wasa-tartine-croustillante-fibres',
            categories='Aliments et boissons à base de végétaux,'\
                'Aliments d\'origine végétale, Céréales et pommes de terre,'
                ' Pains, Biscottes, Pains croustillants',
            category_id=1
        )
        Product.objects.create(
            id=3,
            id_origin = 'zeregrt',
            name = 'Croustillant Chocolat - Bjorg - 500 g',
            nutriscore_grade = 'C',
            fat = 17,
            saturated_fat = 4.3,
            sugar= 15,
            salt= 0.03,
            image='https://static.openfoodfacts.org/images/products/322/982/016/0672/front_fr.248.400.jpg',
            url='https://fr.openfoodfacts.org/produit/3229820160672/croustillant-chocolat-bjorg',
            categories='Aliments et boissons à base de végétaux,'\
                ' Aliments d\'origine végétale,'\
                ' Céréales et pommes de terre,'\
                ' Petit-déjeuners, Céréales et dérivés,'\
                ' Céréales pour petit-déjeuner, Céréales au chocolat,'\
                ' Pépites de céréales croustillantes,'\
                ' Pépites de céréales au chocolat',
            category_id=1
        )

    def test_product_with_instance(self):
        product = Product.objects.get(pk=1)
        self.assertIsInstance(product, Product)
        self.assertEquals(product.id, 1)
        self.assertEquals(product.id_origin, "fevfvf")
        self.assertEquals(
            product.name,
            "Pain 100% mie nature PT - Harrys - 500 g"
        )
        self.assertEquals(product.nutriscore_grade, "B")
        self.assertEquals(float(product.fat), 4.3)
        self.assertEquals(float(product.saturated_fat), 0.4)
        self.assertEquals(float(product.sugar), 7.7)
        self.assertEquals(float(product.salt), 1.13)
        self.assertEquals(
            product.image,
            'https://static.openfoodfacts.org/images/products/322/885/'\
            '700/0852/front_fr.134.400.jpg'
        )
        self.assertEquals(
            product.url,
            'https://fr.openfoodfacts.org/produit/3228857000852/'\
            'pain-100-mie-nature-pt-harrys'
        )
        self.assertEquals(
            product.categories,
            'Aliments et boissons à base de végétaux,'\
                'Aliments d\'origine végétale, Céréales et pommes de terre,'\
                'Pains, Pains de mie, Pains de mie sans croûte'
        )
        self.assertEquals(product.category.id, 1)
