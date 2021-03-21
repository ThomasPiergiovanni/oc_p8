""" Connection manager module
"""
import requests


class ConnectionManager:
    """
    """
    CATEGORIES_ENDPOINT = "https://fr.openfoodfacts.org/categories.json"
    SELECTED_CATEGORIES = ["en:snacks", "en:desserts", "en:breads",
                       "en:breakfast-cereals", "en:meals"]
    PRODUCTS_AMOUNT = 50

    def __init__(self):
        self.endpoint = None
        self.params = None

    def download_categories(self):
        """
        """
        try:
            endpoint = "https://fr.openfoodfacts.org/categories.json"
            payload = {}
            header = {}
            response = requests.get(endpoint, headers=header, data=payload)
            response_json = response.json()
            print(response_json)
        except:
            pass
            print("problem")

    def download_products(self):
        """
        """
        try:
            self.endpoint = "https://fr.openfoodfacts.org/cgi/search.pl"
            self.params = {
            "action": "process", "tagtype_0": "categories",
            "tag_contains_0": "contains", "tag_0": category.id_origin,
            "json": 1, "page": 1, "page_size": PRODUCTS_AMOUNT}
            pass
        except:
            pass
    



if __name__ == "__main__":
    connection_manager = ConnectionManager()
    connection_manager.download_categories()