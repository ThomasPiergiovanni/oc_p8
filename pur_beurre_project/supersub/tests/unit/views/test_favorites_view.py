from django.contrib import messages
from django.test import TestCase, RequestFactory
from django.contrib.auth import authenticate, login, logout

from authentication.models import CustomUser
# from supersub.models import Category, Product, Favorites
from supersub.models.category import Category
from supersub.models.product import Product
from supersub.models.favorites import Favorites

from supersub.views.favorites_view import FavoritesView

from supersub.tests.unit.managers.test_supersub_manager import SupersubManagerTest


class TestFavoritesView(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        cls.favorites_view = FavoritesView()
        SupersubManagerTest.emulate_category()
        cls.emulate_product()
        cls.emulate_custom_user()
        cls.custom_user = CustomUser.objects.get(pk=1)
    
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

    # @classmethod
    # def emulate_category(cls):
    #     Category.objects.create(
    #         id=1,
    #         name="CategorieOne",
    #         url="www.categorie_test.com")

    @classmethod
    def emulate_custom_user(cls):
        CustomUser.objects.create_user(
                id=1,
                email='testuser@email.com',
                password='_Xxxxxxx',
                first_name='tester')
    
    
    def emulate_favorites(self):
        Favorites.objects.create(product_id=1, custom_user_id=1)

    def test___init__with_favorites(self):
        self.assertTrue(self.favorites_view)
    
    def test__init__with_attr_data_render(self):
        self.assertEqual(
            self.favorites_view.data['render'],
            'supersub/favorites.html')
    
    def test__init__with_attr_data_redirect(self):
        self.assertEqual(
            self.favorites_view.data['redirect'],
            'supersub:index')
    
    def test_get_with_response_200_with_favs_and_logged_in(self):
        self.emulate_favorites()
        self.client.login(email='testuser@email.com', password='_Xxxxxxx')
        response = self.client.get('/supersub/favorites/')
        self.assertEqual(response.status_code, 200)
    
    def test_get_with_favorite(self):
        self.emulate_favorites()
        self.client.login(email='testuser@email.com', password='_Xxxxxxx')
        response = self.client.get('/supersub/favorites/')
        self.assertEqual(response.context['page_obj'][0].custom_user_id, 1)
    
    def test_get_with_message_warning(self):
        self.client.login(
            email='testuser@email.com',
            password='_Xxxxxxx')
        response = self.client.get('/supersub/favorites/', follow=True)
        messages = response.context['messages']
        for message in messages:
            self.assertEqual(message.level_tag, 'warning')
            self.assertEqual(message.message, "Vous n'avez enregistré aucun"\
            " favoris jusqu'à présent")

    def test_get_with_message_error(self):
        response = self.client.get('/supersub/favorites/', follow=True)
        messages = response.context['messages']
        for message in messages:
            self.assertEqual(message.level_tag, 'error')
            self.assertEqual(message.message, "Connectez-vous pour"\
            " consulter vos favoris!")