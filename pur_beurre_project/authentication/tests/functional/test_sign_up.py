"""Module for sign up use case functional test
"""
from time import sleep

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from authentication.tests.unit.models.test_custom_user import CustomUserTest


class SignUpTest(StaticLiveServerTestCase):
    """Sign up use case test class
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Edge(
            'C:\Program Files\EdgeDriver\msedgedriver.exe'
        )
        cls.browser.implicitly_wait(10)
        CustomUserTest().emulate_custom_user()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()
    
    def setUp(self):
        # The user logs to the sign up page
        self.browser.get('%s%s' % (
            self.live_server_url,
            '/authentication/sign_up/'
        ))
    
    def test_sign_up_use_case(self):
        # The user types its email on the main form
        sleep(2)
        self.browser.find_element_by_id('id_first_name_form').send_keys('tester')
        sleep(2)