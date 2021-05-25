from django.test import TestCase, RequestFactory

from supersub.manager.off_api_manager import OffApiManager


class OffApiManagerTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        cls.emulate_categories_response()
    
    @classmethod
    def emulate_categories_response(cls):
        cls.categories_response = {
            "count": 19982,
            "tags": [
                {
                    "id": "en:snacks",
                    "known": 1,
                    "name": "Snacks",
                    "products": 54568,
                    "url": "https://fr.openfoodfacts.org/categorie/snacks"
                },
                {
                    "id": "en:plant-based-foods",
                    "known": 1,
                    "name": "Aliments d'origine végétale",
                    "products": 92254,
                    "url": "https://fr.openfoodfacts.org/categorie/aliments-d-origine-vegetale"
                }
            ]
        }

    # def test_download_catgories_with_mock(self):

    #     class EmulateGetRequest:
    #         def __init__(self, endpoint=None, params=None):
    #             self.category_endpoint = None
    #             self.parameters = None
    #             self.response = None
            
    #         def get(self, endpoint=None, params=None):
    #             self.category_endpoint = endpoint
    #             self.parameters = params
    #             return response

    #         def json(self):
    #             """Method returning a json object
    #             """
    #             self.response = True
    #             return self.response

    #     OffApiManager.download_categories = EmulateGetRequest
    #     api_off = OffApiManager()
    #     api_off.download_categories()
    #     self.assertTrue(api_off.response)

    def test_filter_categories_with_raw_datas(self):
        manager = OffApiManager()
        manager.categories_response = self.categories_response
        manager.filter_categories()
        self.assertEqual(manager.categories[0]['id'], "en:snacks")
    

        