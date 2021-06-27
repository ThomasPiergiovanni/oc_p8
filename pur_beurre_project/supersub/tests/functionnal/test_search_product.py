from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from time import sleep


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
    
    def setUp(self):
        # The user logs to the app page
        self.browser.get('%s%s' % (self.live_server_url, '/supersub/'))
    
    def test_user_lands_on_home_page(self):
        # The user notices the page name and the header title
        self.assertIn("P8 - Pur-beurre", self.browser.title)
        self.assertIn(
            'DU GRAS, OUI MAIS DE QUALITÉ',
            self.browser.find_element_by_tag_name('h1').text
        )

        # The user notices a navbar composed of an image 
        navbar_image = self.browser.find_element_by_tag_name('img')
        self.assertEqual(
            navbar_image.get_attribute('src'),
            '*/static/supersub/assets/img/'\
            'logo_pur_beurre.png'
        )

        #...  a title
        navbar_text = self.browser.find_element_by_id(
            'navbar_pur_beurre_texte'
        ).text
        self.assertIn("Pur Beurre",navbar_text)

        #... a form
        navbar_inputbox = self.browser.find_element_by_id(
            'navbar_search_form'
        )
        self.assertEqual(navbar_inputbox.get_attribute('method'),'post')

        # ... a user, a carrot and a logout icons
        self.assertTrue(self.browser.find_element_by_id('user_icon'))
        self.assertTrue(self.browser.find_element_by_id('carrot_icon'))
        self.assertTrue(self.browser.find_element_by_id('logout_icon'))

    def test_search_product_use_case(self):
        # The user types "Pain" on teh main form
        sleep(2)
        self.browser.find_element_by_id('id_main_form').send_keys('Pain')
        sleep(5)

        # The user clicks then "Chercher" button"
        self.browser.find_element_by_id('index_search_button').click()
        sleep(2)
        # self.assertTrue(
        #     self.browser.find_element_by_id('result_searched_product')
        # )
