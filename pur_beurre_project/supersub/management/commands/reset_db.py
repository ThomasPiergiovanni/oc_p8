# pylint: disable=E1101,R0201
""" DB management command
"""
from django.core.management.base import BaseCommand

from supersub.management.client.off_api_manager import OffApiManager
from supersub.models.category import Category
from supersub.models.product import Product
from supersub.models.favorites import Favorites
from authentication.models import CustomUser


class Command(BaseCommand):
    """ Reset DB from scratch by making request to OFF API. Use it with
    option --all to reset all users as well. This including superuser
    """
    help = "Reset DB from scratch by making request to OFF API. Use it with"\
        " option --all to reset all users as well. This including superuser"

    def __init__(self):
        super().__init__()
        self.categories_in_db = []
        self.off_api_manager = OffApiManager()

    def add_arguments(self, parser):
        parser.add_argument(
            '--all',
            action='store_true',
            help='Reset all db values including users and superusers'
        )

    def handle(self, *args, **options):
        self.drop_categories()
        self.drop_products()
        self.drop_favorites()
        self.off_api_manager.download_categories()
        self.off_api_manager.filter_categories()
        self.insert_categories()
        self.get_categories()
        self.insert_products()
        if options['all']:
            self.drop_users()

    def drop_categories(self):
        """Method thats drop categories entities from DB
        """
        self._drop_objects(Category)

    def _drop_objects(self, object_class):
        """Manager method thats drop objects entities from DB
        """
        objects = object_class.objects.all()
        objects.delete()

    def get_categories(self):
        """Method thats select all categories entities from DB
        """
        all_categories = Category.objects.all()
        for category in all_categories:
            self.categories_in_db.append(category)

    def insert_categories(self):
        """Method that uses categories entities collected by OFF API manager
        and insert those entities into DB.
        """
        for raw_category in self.off_api_manager.categories:
            category = Category(
                id_origin=raw_category['id'],
                name=raw_category['name'],
                url=raw_category['url']
            )
            category.save()

    def drop_products(self):
        """Method thats drops products entities from DB
        """
        self._drop_objects(Product)

    def insert_products(self):
        """Method that uses products entities collected by OFF API manager
        and insert those entities into DB.
        """
        unique_prods_list = []
        for category in self.categories_in_db:
            self.off_api_manager.download_products(category)
            self.off_api_manager.filter_products()
            for raw_product in self.off_api_manager.products:
                if raw_product['product_name'] not in unique_prods_list:
                    product = Product(
                        id_origin=raw_product['id'],
                        name=raw_product['product_name'],
                        nutriscore_grade=raw_product['nutriscore_grade'],
                        fat=raw_product['nutriments']['fat_100g'],
                        saturated_fat=(
                            raw_product['nutriments']['saturated-fat_100g']
                        ),
                        sugar=raw_product['nutriments']['sugars_100g'],
                        salt=raw_product['nutriments']['salt_100g'],
                        image=raw_product['image_small_url'],
                        url=raw_product['url'],
                        categories=raw_product['categories_hierarchy'],
                        category_id=category.id
                    )
                    product.save()
                    unique_prods_list.append(raw_product['product_name'])

    def drop_favorites(self):
        """Method thats drops favorites entities from DB
        """
        self._drop_objects(Favorites)

    def drop_users(self):
        """Method thats drops users entities from DB
        """
        self._drop_objects(CustomUser)
