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

    def test___init__with_attr_manager_are_true(self):
        self.assertTrue(self.custom_view.manager)
        self.assertTrue(self.custom_view.data)
        self.assertTrue(self.custom_view.data['ctxt']['main_form'])
        self.assertTrue(self.custom_view.data['ctxt']['navbar_form'])
        self.assertEqual(self.custom_view.data['ctxt']['searched_prod'], '')
        self.assertEqual(self.custom_view.data['ctxt']['prod'], '')
        self.assertEqual(self.custom_view.data['ctxt']['page_obj'], '')
        self.assertEqual(self.custom_view.data['ctxt']['user'], '')
        self.assertEqual(self.custom_view.data['ctxt']['form'], '')
        self.assertEqual(self.custom_view.data['render'], '')
        self.assertEqual(self.custom_view.data['redirect'], '')
    
    def test___init__with_attr_manager_type(self):
        self.assertEqual(type(self.custom_view.manager), type(self.manager))
    
    def test___init__with_attr_data_ctxt_mainform_type(self):
        self.assertEqual(
            type(self.custom_view.data['ctxt']['main_form']),
            type(MainSearchForm()))

    def test___init__with_attr_data_ctxt_mainform_type(self):
        self.assertEqual(
            type(self.custom_view.data['ctxt']['navbar_form']),
            type(NavbarSearchForm()))
            
