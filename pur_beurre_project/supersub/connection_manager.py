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
        self.cat_response = None

    def download_categories(self):
        """
        """
        try:
            endpoint = "https://fr.openfoodfacts.org/categories.json"
            payload = {}
            header = {}
            response = requests.get(endpoint, headers=header, data=payload)
            self.cat_response = response.json()
            # print(self.cat_response)
        except:
            pass
            print("problem")

#{'known': 0, 'id': 'fr:vinaigre-au-combava', 'name': 'vinaigre-au-combava', 'url': 'https://fr.openfoodfacts.org/categorie/vinaigre-au-combava', 'products': 2}

    def filter_categories(self, selected_categories = SELECTED_CATEGORIES):
        
        try:
            for categories in self.cat_response["tags"]:
                if categories["id"] in selected_categories and \
                        categories["name"] and categories["url"]:
                    valid_category = (
                        categories["id"], categories["name"], categories["url"])
                    print(valid_category)
            # for category in categories:
            #     print(category)
                # if category["id"] in SELECTED_CATEGORIES and \
                #         category["name"] and category["url"]:
                #     valid_category = (
                #         category["id"], category["name"], category["url"])
                #     print(category["name"])
        except KeyError:
            pass

    def download_products(
            self, selected_categories = SELECTED_CATEGORIES,
            product_amount = PRODUCTS_AMOUNT):
        """
        """
        try:
            for category in selected_categories:
                endpoint = "https://fr.openfoodfacts.org/cgi/search.pl?"  
                params = {
                    "action": "process", "tagtype_0": "categories",
                    "tag_contains_0": "contains", "tag_0": category,
                    "json": 1, "page": 1, "page_size": PRODUCTS_AMOUNT}
                header = {}
                response_api = requests.get(endpoint, headers=header, params=params)
                result = response_api.json()
                print(result)


        except TypeError as error:
            print(error)
            pass
    


if __name__ == "__main__":
    connection_manager = ConnectionManager()
    # connection_manager.download_categories()
    # connection_manager.filter_categories()
    connection_manager.download_products()