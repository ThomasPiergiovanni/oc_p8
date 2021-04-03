""" DB manager module
"""

from supersub.off_api_manager import OffApiManager
from supersub.models import Category, Product


class DbManager():
    """
    """
    def __init__(self):
        self.selected_categories = ["en:snacks", "en:desserts", "en:breads",
                "en:breakfast-cereals", "en:meals"]
        self.categories_in_db = []
        self.drop_categories()
        self.get_categories()
        self.insert_categories()
        self.products_in_db = []
        self.drop_products()
        self.get_products()
        self.insert_products()
    
    def drop_categories(self):
        """
        """
        all_categories = Category.objects.all()
        all_categories.delete()

    
    def get_categories(self):
        """
        """
        self.categories_in_db = []
        all_categories = Category.objects.all()
        for category in all_categories:
            self.categories_in_db.append(category)
    
    def insert_categories(self):
        """
        """
        off_api_manager = OffApiManager()
        off_api_manager.download_categories()
        for raw_data in off_api_manager.categories:
            for raw_category in raw_data['tags']:
                try:
                    if (
                        raw_category['id'] in self.selected_categories and
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
                except KeyError as error:
                    print(error)

    def drop_products(self):
        """
        """
        all_products = Product.objects.all()
        all_products.delete()

    def get_products(self):
        """
        """
        self.products_in_db = []
        all_product = Product.objects.all()
        for product in all_product:
            self.products_in_db.append(product.name)

    def insert_products(self):
        """
        """
        self.get_categories()
        for category in self.categories_in_db:
            off_api_manager = OffApiManager()
            off_api_manager.download_products(category)
            raw_data = off_api_manager.products
            for products_category in raw_data:
                for raw_product in products_category['products']:
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
                                self.products_in_db.append(product.name)
                                product.save()
                    except KeyError as error:
                        print(error)
