from selenium import webdriver

from django.test import TestCase

class NewVisitorTest(TestCase):
    """
    """
    def setUp(self):
        self.browser = webdriver.Edge('C:\Program Files\EdgeDriver\msedgedriver.exe')
        self.browser = webdriver.Edge()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_index_has_correct_title(self):
        self.browser.get('http://127.0.0.1:8000/supersub')
        self.assertIn("P8 - Pur-beurre", self.browser.title)
    