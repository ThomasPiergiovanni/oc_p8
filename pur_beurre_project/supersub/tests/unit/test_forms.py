from django.test import TestCase

from supersub.forms.main_search_form import MainSearchForm
from supersub.forms.navbar_search_form import NavbarSearchForm


class FormsTest(TestCase):
    """
    """
    def setUp(self):
        self.main_form = MainSearchForm()
    
    def test_main_form_product_field_if_label_is_none(self):
        self.assertTrue(self.main_form.fields['product'].label == None)
    
    def test_main_form_product_field_if_class_is_form_control(self):
        self.assertTrue(
            self.main_form.fields['product']
            .widget.attrs['class'] =='form-control')
    
    def test_main_form_product_field_if_autofocus_is_true(self):
        self.assertTrue(
            self.main_form.fields['product']
            .widget.attrs['autofocus'] is True)
    
    def test_form_validation_for_blank_product(self):
        form = MainSearchForm(data={'product':''})
        self.assertFalse(form.is_valid())
