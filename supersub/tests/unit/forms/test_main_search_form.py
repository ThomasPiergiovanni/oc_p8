# pylint: disable=C0116
"""Test main search form module.
"""
from django.test import TestCase

from supersub.forms.main_search_form import MainSearchForm


class MainSearchFormTest(TestCase):
    """Test main search form class.
    """
    def setUp(self):
        self.main_form = MainSearchForm()

    def test_mainsearchform_with_attr_product_label(self):
        self.assertTrue(self.main_form.fields['product'].label is None)

    def test_mainsearchform_with_attr_product_class(self):
        self.assertTrue(
            self.main_form.fields['product']
            .widget.attrs['class'] == 'form-control')

    def test_mainsearchform_with_attr_product_autofocus(self):
        self.assertTrue(
            self.main_form.fields['product']
            .widget.attrs['autofocus'] is True)

    def test_mainsearchform_with_validation_wo_input(self):
        form = MainSearchForm(data={'product': ''})
        self.assertFalse(form.is_valid())

    def test_mainsearchform_with_validation_with_input(self):
        form = MainSearchForm(data={'product': 'Un produit test'})
        self.assertTrue(form.is_valid())
