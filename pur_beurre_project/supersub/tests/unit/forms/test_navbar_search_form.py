# pylint: disable=C0116
"""Test navbar search form module.
"""
from django.test import TestCase

from supersub.forms.navbar_search_form import NavbarSearchForm


class NavbarSearchFormTest(TestCase):
    """Test navbar search form class.
    """
    def setUp(self):
        self.form = NavbarSearchForm()

    def test_navbarsearchform_with_attr_product_label(self):
        self.assertTrue(self.form.fields['product'].label is None)

    def test_navbarsearchform_with_attr_product_class(self):
        self.assertTrue(
            self.form.fields['product']
            .widget.attrs['class'] =='form-control mybox')

    def test_navbarsearchform_with_attr_product_autofocus(self):
        self.assertRaises(
            KeyError,
            lambda: self.form.fields['product'].widget.attrs['autofocus'])

    def test_navbarsearchform_with_validation_wo_input(self):
        form = NavbarSearchForm(data={'product':''})
        self.assertFalse(form.is_valid())

    def test_navbarsearchform_with_validation_with_input(self):
        form = NavbarSearchForm(data={'product':'Un produit test'})
        self.assertTrue(form.is_valid())
