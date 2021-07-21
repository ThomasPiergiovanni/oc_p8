# pylint: disable=C0116, W0212
"""Test custom view module.
"""
from django.test import TestCase

from supersub.forms.main_search_form import MainSearchForm
from supersub.forms.navbar_search_form import NavbarSearchForm
from supersub.views.custom_view import CustomView


class TestCustomView(TestCase):
    """Test custom view class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.custom_view = CustomView()

    def test_customview_with_customview(self):
        self.assertTrue(self.custom_view)

    def test_customview_with_attr_manager_are_true(self):
        self.assertTrue(self.custom_view._data)
        self.assertTrue(self.custom_view._data['ctxt']['main_form'])
        self.assertTrue(self.custom_view._data['ctxt']['navbar_form'])
        self.assertEqual(self.custom_view._data['ctxt']['searched_prod'], '')
        self.assertEqual(self.custom_view._data['ctxt']['prod'], '')
        self.assertEqual(self.custom_view._data['ctxt']['page_obj'], '')
        self.assertEqual(self.custom_view._data['ctxt']['user'], '')
        self.assertEqual(self.custom_view._data['ctxt']['form'], '')
        self.assertEqual(self.custom_view._data['render'], '')
        self.assertEqual(self.custom_view._data['redirect'], '')

    def test_customview_with_attr_data_ctxt_mainform_type(self):
        self.assertEqual(
            type(self.custom_view._data['ctxt']['main_form']),
            type(MainSearchForm())
        )

    def test_customview_with_attr_data_ctxt_navbarform_type(self):
        self.assertEqual(
            type(self.custom_view._data['ctxt']['navbar_form']),
            type(NavbarSearchForm())
        )
