""" Off api manager manager module
"""

import requests


class OffApiManager:
    """
    """
    def __init__(self):
        self.category_endpoint = "https://fr.openfoodfacts.org/categories.json"
        self.selected_categories = ["en:snacks", "en:desserts", "en:breads",
            "en:breakfast-cereals", "en:meals"]
        self.product_endpoint = "https://fr.openfoodfacts.org/cgi/search.pl?"
        self.header = {}
        self.parameters = {}
        self.products_amount = 1
        self.cat_response = {}
        self.categories = []
        self.prod_response = {}
        self.products = []
    
    def download_categories(self):
        """
        """
        response = requests.get(
            self.category_endpoint,
            headers=self.header,
            params=self.parameters
        )
        self.cat_response = response.json()
    
    def filter_categories(self):
        """
        """
        for raw_category in self.cat_response['tags']:
            try:
                if (
                    raw_category['id'] in self.selected_categories and
                    raw_category['id'] not in self.categories and
                    raw_category['id'] and
                    raw_category['name'] and
                    raw_category['url']
                ):
                    self.categories.append(raw_category)
            except KeyError as error:
                print("Category key error:", error)

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
        self.prod_response = response.json()
    
    def filter_products(self):
        """
        """
        for raw_product in self.prod_response['products']:
            try:
                if (
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
                    self.products.append(raw_product)
            except KeyError as error:
                print("Product key error: ", error)
