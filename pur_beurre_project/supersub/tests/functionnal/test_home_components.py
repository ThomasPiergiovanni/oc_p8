# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# from django.test import LiveServerTestCase

# class NewSearchTest(LiveServerTestCase):
#     """
#     """
#     def setUp(self):
#         self.browser = webdriver.Edge(
#             'C:\Program Files\EdgeDriver\msedgedriver.exe'
#         )
#         self.browser.get('http://127.0.0.1:8000/supersub')
    
#     def tearDown(self):
#         self.browser.quit()
    
#     def test_index_head_tags(self):
#         # The user logs to the app page


#         # The user notices the page name and the header title
#         self.assertIn("P8 - Pur-beurre", self.browser.title)
#         header_h1_text = self.browser.find_element_by_tag_name('h1').text
#         self.assertIn('DU GRAS, OUI MAIS DE QUALITÉ', header_h1_text)
    
#     def test_index_navbars_tags(self):
#         # The user logs to the app page
#         # self.browser.get('http://127.0.0.1:8000/supersub')

#         # The user notices a navbar composed of an image, a title,
#         # a form, a user icon, a food prod icon and a logout session icon
#         navbar_image = self.browser.find_element_by_tag_name('img')
#         self.assertEqual(
#             navbar_image.get_attribute('src'),
#             'http://127.0.0.1:8000/static/supersub/assets/img/'\
#             'logo_pur_beurre.png'
#         )
#         navbar_text = self.browser.find_element_by_id(
#             'navbar_pur_beurre_texte'
#         ).text
#         self.assertIn("Pur Beurre", navbar_text)
#         navbar_inputbox = self.browser.find_element_by_id(
#             'navbar_search_form'
#         )
#         self.assertEqual(navbar_inputbox.get_attribute('method'),'post')
#         self.assertTrue(self.browser.find_element_by_id('user_icon'))
#         self.assertTrue(self.browser.find_element_by_id('carrot_icon'))
#         self.assertTrue(self.browser.find_element_by_id('logout_icon'))
    
#     def test_index_header_tags(self):
#         # The user logs to the app page
#         # self.browser.get('http://127.0.0.1:8000/supersub')

#         # The user notices a form textbox as well as a search button
#         main_inputbox = self.browser.find_element_by_id(
#             'index_main_search_form'
#         )
#         self.assertEqual(main_inputbox.get_attribute('method'),'post')
#         button = self.browser.find_element_by_id('index_search_button')
#         self.assertEqual(button.get_attribute('type'),'submit')
    
#         # Above the form, the user sees a message invinting to look for 
#         # a substitutes products from the ones he usually consume
#         header_h2_text = self.browser.find_element_by_tag_name('h2').text
#         self.assertIn(
#             'Trouvez un produit de substitution pour ceux que vous '\
#             'consommez tous les jours!', header_h2_text
#         )

#     def test_user_case_search_a_product_and_gets_a_list_of_subs(self):
#         # The user logs to the app page
#         # self.browser.get('http://127.0.0.1:8000/supersub')

#         # The user types "Pain" into the main input box
#         main_inputbox = self.browser.find_element_by_id(
#             'index_main_search_form'
#         )
#         main_inputbox.send_keys("Pain")

#         # When the user hits enter a new page is open with the products
#         # and ther subs prodcuts
#         main_inputbox.send_keys(Keys.ENTER)
#         time.sleep(10)
#         self.assertTrue(
#             self.browser.find_element_by_id('result_searched_product')
#         )

    