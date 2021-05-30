""" DB manager module
"""

from supersub.manager.off_api_manager import OffApiManager
from supersub.models.category import Category
from supersub.models.product import Product
from supersub.models.favorites import Favorites
from authentication.models import CustomUser


class DbManager():
    """
    """
    def __init__(self):
        self.categories_in_db = []
        self.off_api_manager = OffApiManager()
    
    def reset_db(self, reset_user=False):
        """
        """
        self.drop_categories()
        self.drop_products()
        self.drop_favorites()
        self.off_api_manager.download_categories()
        self.off_api_manager.filter_categories()
        self.insert_categories()
        self.get_categories()
        self.insert_products()
        if reset_user:
            self.drop_users()

    def drop_categories(self):
        """
        """
        all_categories = Category.objects.all()
        all_categories.delete()

    def get_categories(self):
        """
        """
        all_categories = Category.objects.all()
        for category in all_categories:
            self.categories_in_db.append(category)
    
    def insert_categories(self):
        """
        """
        for raw_category in self.off_api_manager.categories:
            category = Category(
                id_origin = raw_category['id'],
                name = raw_category['name'],
                url = raw_category['url']
            )
            category.save()

    def drop_products(self):
        """
        """
        all_products = Product.objects.all()
        all_products.delete()
    
    def insert_products(self):
        """
        """
        unique_prods_list =[]
        for category in self.categories_in_db:
            self.off_api_manager.download_products(category)
            self.off_api_manager.filter_products()
            for raw_product in self.off_api_manager.products:
                if raw_product['product_name'] not in unique_prods_list:
                    product = Product(
                        id_origin = raw_product['id'],
                        name = raw_product['product_name'],
                        nutriscore_grade = raw_product['nutriscore_grade'],
                        fat = raw_product['nutriments']['fat_100g'],
                        saturated_fat = raw_product['nutriments']['saturated-fat_100g'],
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
        """
        """
        all_favorites = Favorites.objects.all()
        all_favorites.delete()
    
    def drop_users(self):
        """
        """
        all_users = CustomUser.objects.all()
        all_users.delete()
