from selenium import webdriver

from django.test import TestCase

class NewSearchTest(TestCase):
    """
    """
    def setUp(self):
        self.browser = webdriver.Edge(
            'C:\Program Files\EdgeDriver\msedgedriver.exe'
        )
    
    def tearDown(self):
        self.browser.quit()
    
    def test_user_can_search_a_product_and_gets_a_list_of_subs(self):
        # The user logs to our app page
        self.browser.get('http://127.0.0.1:8000/supersub')

        # The user notices the page name and the header title
        self.assertIn("P8 - Pur-beurre", self.browser.title)
        header_h1_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('DU GRAS, OUI MAIS DE QUALITÉ', header_h1_text)

        # The user notices a navbar composed of an image,
        # a user icon, a food prod icon and a logout session icon
        navbar_image = self.browser.find_element_by_tag_name('img')
        self.assertEqual(
            navbar_image.get_attribute('src'),
            'http://127.0.0.1:8000/static/supersub/assets/img/'\
            'logo_pur_beurre.png'
        )

        #... a title
        navbar_text = self.browser.find_element_by_id(
            'navbar_pur_beurre_texte'
        ).text
        self.assertIn("Pur Beurre", navbar_text)

        # ...a form
        navbar_inputbox = self.browser.find_element_by_id(
            'navbar_search_form'
        )
        self.assertEqual(navbar_inputbox.get_attribute('method'),'post')

        # ...an icon representing a user
        navbar_user= self.browser.find_element_by_id('user_icon')
        self.assertTrue(navbar_user)
        
        # ...an icon representing a carrot (its for the user favorites)
        navbar_carrot= self.browser.find_element_by_id('carrot_icon')
        self.assertTrue(navbar_carrot)

        # ...and an icon representing logout
        navbar_logout= self.browser.find_element_by_id('logout_icon')
        self.assertTrue(navbar_logout)

        # The user notices a form textbox as well as a search button
        inputbox = self.browser.find_element_by_id('index_main_search_form')
        self.assertEqual(inputbox.get_attribute('method'),'post')
        button = self.browser.find_element_by_id('index_search_button')
        self.assertEqual(button.get_attribute('type'),'submit')
    
        # Above the form, the user sees a message invinting to look for 
        # a substitutes products from the ones he usually consume
        header_h2_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn(
            'Trouvez un produit de substitution pour ceux que vous '\
            'consommez tous les jours!', header_h2_text
        )

    