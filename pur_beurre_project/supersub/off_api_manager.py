""" Off api manager manager module
"""

import requests



class OffApiManager:
    """
    """

    SELECTED_CATEGORIES = ["en:snacks", "en:desserts", "en:breads",
                       "en:breakfast-cereals", "en:meals"]
    PRODUCTS_AMOUNT = 1

    def __init__(self):
        self.endpoint = "https://fr.openfoodfacts.org/cgi/search.pl?"
        self.params = None
        self.categories = ["en:snacks", "en:desserts", "en:breads",
                       "en:breakfast-cereals", "en:meals"]
        self.products_amount = 1
        self.cat_response = None

    def download_products(self):
        """
        """
        try:
            for category in self.categories: 
                params = {
                    "action": "process", "tagtype_0": "categories",
                    "tag_contains_0": "contains", "tag_0": category,
                    "json": 1, "page": 1, "page_size": self.products_amount}
                header = {}
                response_api = requests.get(self.endpoint, headers=header, params=params)
                result = response_api.json()
                print(result)


        except TypeError as error:
            print(error)
            pass
    


if __name__ == "__main__":
    off_api_manager = OffApiManager()
    # connection_manager.download_categories()
    # connection_manager.filter_categories()
    off_api_manager.download_products()