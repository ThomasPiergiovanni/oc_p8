""" DB manager module
"""

from supersub.off_api_manager import OffApiManager
from supersub.models import Category, Product


class DbManager():
    """
    """
    def __init__(self):
        off_api_manager = OffApiManager()
        off_api_manager.download_categories()
        off_api_manager.download_products()
        self.drop_categories()
        self.drop_products()
        self.off_categories = off_api_manager.categories
        self.categories_in_db = []
        self.products = off_api_manager.products
        self.products_in_db = []
    
    def drop_categories(self):
        all_categories = Category.objects.all()
        all_categories.delete()
    
    def get_categories(self):
        all_categories = Category.objects.all()
        for category in all_categories:
            self.categories_in_db.append(category)
    
    def insert_categories(self):
        """
        """
        self.get_categories()
        for category in self.off_categories:
            for raw_category in category['tags']:
                try:
                    if (
                        raw_category['id'] not in self.categories_in_db and
                        raw_category['id'] and
                        raw_category['name'] and
                        raw_category['url']
                    ):
                        category = Category(
                            id_origin = raw_category['id'],
                            name = raw_category['name'],
                            url = raw_category['url']
                        )
                        self.categories_in_db.append(category.name)
                        category.save()
                except Error as error:
                    print(error)

    def drop_products(self):
        """
        """
        all_products = Product.objects.all()
        all_products.delete()

    def get_products(self):
        all_product = Product.objects.all()
        for product in all_product:
            self.products_in_db.append(product.name)

    def insert_products(self):
        self.get_categories()
        self.get_products()
        for category in categories_in_db:

        for category in self.products:
            for raw_product in category['products']:
                try:
                    if (
                            raw_product['product_name'] not in self.products_in_db and
                            raw_product['id'] and
                            raw_product['product_name'] and
                            raw_product['nutriscore_grade'] and
                            raw_product['nutriments']['fat_100g'] and
                            raw_product['nutriments']['saturated-fat_100g'] and
                            raw_product['nutriments']['sugars_100g'] and
                            raw_product['nutriments']['salt_100g'] and
                            raw_product['image_small_url'] and
                            raw_product['url'] and
                            raw_product['categories_hierarchy']
                    ):
                        category_id = [category.id_origin for category in self.categories_in_db if category.origin_id == raw_product['categories_hierarchy'][0]]
                        print(category_id)
                        product = Product(
                            id_origin=raw_product['id'],
                            name=raw_product['product_name'],
                            nutriscore_grade=raw_product['nutriscore_grade'],
                            fat=raw_product['nutriments']['fat_100g'],
                            saturated_fat=raw_product['nutriments']['saturated-fat_100g'],
                            sugar=raw_product['nutriments']['sugars_100g'],
                            salt=raw_product['nutriments']['salt_100g'],
                            image=raw_product['image_small_url'],
                            url=raw_product['url'],
                            categories=raw_product['categories_hierarchy']
                            category_id=category_id
                        )
                        self.products_in_db.append(product.name)
                        product.save()
                except Error as error:
                    print(error)

