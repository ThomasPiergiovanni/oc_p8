""" DB manager module
"""

from supersub.off_api_manager import OffApiManager
from supersub.models import Product


class DbManager():
    """
    """
    def __init__(self):
        off_api_manager = OffApiManager()
        off_api_manager.download_products()
        self.source_data = off_api_manager.products
        self.insert_products()

    def insert_products(self):
        for category in self.source_data:
            for raw_product in category['products']:
                try:
                    if (
                            raw_product['id'] and
                            raw_product['product_name'] and
                            raw_product['nutriscore_grade'] and
                            raw_product['nutriments']['fat_100g']
                            # raw_product['saturated-fat_100g'] and
                            # raw_product['sugars_100g'] and
                            # raw_product['salt_100g'] and
                            # raw_product['image_small_url'] and
                            # raw_product['url'] and
                            # raw_product['categories_tags']
                    ):
                        product = Product(
                            id_origin=raw_product['id'],
                            name=raw_product['product_name'],
                            nutriscore_grade=raw_product['nutriscore_grade'],
                            fatty_acids=raw_product['nutriments']['fat_100g'])
                        #     saturated_fatty_acids=raw_product['saturated-fat_100g'],
                        #     sugar=raw_product['sugars_100g'],
                        #     salt=raw_product['salt_100g'],
                        #     image=raw_product['image_small_url'],
                        #     url=raw_product['url'],
                        #     categories=raw_product['categories_tags']
                        print(product.id_origin,
                            product.name,
                            product.nutriscore_grade,
                            product.fatty_acids)
                        #product.save()
                except KeyError:
                    pass
    
    def get_products(self):
        pass
