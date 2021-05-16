from django.test import TestCase

from supersub.forms import MainSearchForm, NavbarSearchForm
from supersub.manager.supersub_manager import SupersubManager
from supersub.views.custom_view import CustomView


class TestCustomView(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        cls.custom_view = CustomView()
        cls.manager = SupersubManager()
        cls.data = cls.manager._get_data()

    def test___init__with_customview(self):
        self.assertTrue(self.custom_view)

    def test___init__with_attr_manager_is_true(self):
        self.assertTrue(self.custom_view.manager)
    
    def test___init__with_attr_manager_type(self):
        self.assertEqual(type(self.custom_view.manager), type(self.manager))
    
    def test___init__with_attr_data_type(self):
        self.assertEqual(
            type(self.custom_view.data['ctxt']['main_form']),
            type(MainSearchForm()))
