from django.test import TestCase

from supersub.forms import MainSearchForm, NavbarSearchForm


class FormsTest(TestCase):
    """
    """
    def setUp(self):
        self.main_form = MainSearchForm()
    
    def test_main_form_product_field_label_is_none(self):
        self.assertTrue(self.main_form.fields['product'].label == None)
    
    def test_main_form_product_field_class_is_form_control(self):
        self.assertTrue(
            self.main_form.fields['product']
            .widget.attrs['class'] =='form-control')
    
    def test_main_form_product_field_autofocus_is_true(self):
        self.assertTrue(
            self.main_form.fields['product']
            .widget.attrs['autofocus'] is True)