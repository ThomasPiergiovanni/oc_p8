""" Off api manager manager module
"""

import requests


class OffApiManager:
    """
    """
    def __init__(self):
        self.category_endpoint = "https://fr.openfoodfacts.org/categories.json"
        self.product_endpoint = "https://fr.openfoodfacts.org/cgi/search.pl?"
        self.header = {}
        self.parameters = {}
        self.products_amount = 1
        self.categories = []
        self.products = []
    
    def download_categories(self):
        """
        """
        response = requests.get(
            self.category_endpoint,
            headers=self.header,
            params=self.parameters
        )
        response = response.json()
        self.categories.append(response)

    def download_products(self, category):
        """
        """
        self.parameters = {
            "action": "process", "tagtype_0": "categories",
            "tag_contains_0": "contains", "tag_0": category.id_origin,
            "json": 1, "page": 1, "page_size": self.products_amount
        } 
        response = requests.get(
            self.product_endpoint,
            headers=self.header,
            params=self.parameters
        )
        response = response.json()
        self.products.append(response)

if __name__ == "__main__":
    off_api_manager = OffApiManager()
    off_api_manager.download_products()