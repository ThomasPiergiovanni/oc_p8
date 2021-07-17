# pylint: disable=R0201, R0916
""" OFF API manager module.
"""
import requests

from pur_beurre.custom_settings.custom_settings_functional import (
    CATEGORIES_ENDPOINT,
    SELECTED_CATEGORIES,
    PRODUCTS_ENDPOINT,
    PRODUCTS_AMOUNT
)


class OffApiManager:
    """ OFF API manager class.
    """
    def __init__(self):
        self.categories_response = {}
        self.categories = []
        self.products_response = {}
        self.products = []

    def download_categories(self):
        """ Method that makes a request to OFF API to get catgories.
        """
        response = requests.get(
            CATEGORIES_ENDPOINT,
            headers={},
            params={}
        )
        self.categories_response = response.json()

    def filter_categories(self):
        """ Method that keeps only key compliants catgories.
        """
        for raw_category in self.categories_response['tags']:
            try:
                if (
                    raw_category['id'] in SELECTED_CATEGORIES and
                    raw_category['id'] not in self.categories and
                    raw_category['id'] and
                    raw_category['name'] and
                    raw_category['url']
                ):
                    self.categories.append(raw_category)
            except KeyError:
                pass

    def download_products(self, category):
        """Method that makes a request to OFF API to get products.
        """
        parameters = {
            "action": "process", "tagtype_0": "categories",
            "tag_contains_0": "contains", "tag_0": category.id_origin,
            "json": 1, "page": 1, "page_size": PRODUCTS_AMOUNT
        }
        response = requests.get(
            PRODUCTS_ENDPOINT,
            headers={},
            params=parameters
        )
        self.products_response = response.json()

    def filter_products(self):
        """Method that keeps only key compliants products.
        """
        for raw_product in self.products_response['products']:
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
            except KeyError:
                pass
