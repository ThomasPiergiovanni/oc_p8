""" Off api manager manager module
"""

import requests


class OffApiManager:
    """
    """
    def __init__(self):
        self.product_endpoint = "https://fr.openfoodfacts.org/cgi/search.pl?"
        self.header = {}
        self.parameters = None
        self.categories = ["en:snacks", "en:desserts", "en:breads",
                       "en:breakfast-cereals", "en:meals"]
        self.products_amount = 1
        self.products = []

    def download_products(self):
        """
        """
        for category in self.categories:
            self.parameters = {
                "action": "process", "tagtype_0": "categories",
                "tag_contains_0": "contains", "tag_0": category,
                "json": 1, "page": 1, "page_size": self.products_amount} 
            response = requests.get(
                self.product_endpoint, headers=self.header, params=self.parameters)
            response = response.json()
            self.products.append(response)

if __name__ == "__main__":
    off_api_manager = OffApiManager()
    off_api_manager.download_products()