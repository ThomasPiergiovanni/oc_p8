""" DB manager module
"""
from off_api_manager import OffApiManager


class DbManager:
    """
    """
    def __init__(self):
        off_api_manager = OffApiManager()
        off_api_manager.download_products()
        self.source_data = off_api_manager.products

    def populate_db(self):
        for category in self.source_data:
            for product in category["products"]:
                if product["product_name"]:
                    print(product["product_name"])

if __name__ == "__main__":
    db_manager = DbManager()
    db_manager.populate_db()