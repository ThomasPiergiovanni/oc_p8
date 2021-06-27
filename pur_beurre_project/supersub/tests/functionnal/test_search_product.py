from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from time import sleep

from django.test import LiveServerTestCase

class SearchProductTest(StaticLiveServerTestCase):
    """
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Edge(
            'C:\Program Files\EdgeDriver\msedgedriver.exe'
        )
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()
    

    def test_search_product_use_case(self):
        # The user logs to the app page
        self.browser.get('%s%s' % (self.live_server_url, '/supersub/'))
        # self.assertIn("P8 - Pur-beurre", self.browser.title)

        sleep(5)
    
        # When the user hits enter a new page is open with the products
        # and ther subs prodcuts
        self.browser.find_element_by_id('id_main_form').send_keys('Pain')
        sleep(2)

        self.browser.find_element_by_id('index_search_button').click()
        sleep(2)
        # self.assertTrue(
        #     self.browser.find_element_by_id('result_searched_product')
        # )
