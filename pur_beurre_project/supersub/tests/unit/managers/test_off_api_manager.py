from django.test import TestCase, RequestFactory

from supersub.manager.off_api_manager import OffApiManager


class OffApiManagerTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        pass

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
        