from django.test import TestCase

from authentication.forms.sign_up_form import SignUpForm


class SignUpFormTest(TestCase):
    """
    """
    def setUp(self):
        self.form = SignUpForm()
    
    def test_signupform_with_all_attrs_label(self):
        self.assertTrue(self.form.fields['first_name'].label == "Prénom")
        self.assertTrue(self.form.fields['password1'].label == "Mot de passe")
        self.assertTrue(
            self.form.fields['password2']
            .label == "Confirmer le mot de passe")

    def test_signupform_with_all_attrs_class(self):
        self.assertTrue(
            self.form.fields['first_name']
            .widget.attrs['class'] =='form-control')
        self.assertTrue(
            self.form.fields['email']
            .widget.attrs['class'] =='form-control')
        self.assertTrue(
            self.form.fields['password1']
            .widget.attrs['class'] =='form-control')
        self.assertTrue(
            self.form.fields['password2']
            .widget.attrs['class'] =='form-control')
    
    def test_signupform_with_attr_first_name_autofocus(self):
        self.assertTrue(
            self.form.fields['first_name']
            .widget.attrs['autofocus'] is True)
    
    def test_signupform_with_validation_wo_input(self):
        form = SignUpForm(
            data={
                'first_name':'',
                'email':'',
                'password1':'',
                'password2':'',
                })
        self.assertFalse(form.is_valid())
    
    def test_signupform_with_validation_wrong_email_input(self):
        form = SignUpForm(
            data={
                'first_name':'firname',
                'email':'wrongemail',
                'password1':'_Xxxxxxx',
                'password2':'_Xxxxxxx',
                })
        self.assertFalse(form.is_valid())

    def test_signupform_with_validation_wrong_pswd_input(self):
        form = SignUpForm(
            data={
                'first_name':'firname',
                'email':'correct@email.com',
                'password1':'_Xxxxxxx',
                'password2':'_Zzzzzzz',
                })
        self.assertFalse(form.is_valid())
    
    def test_signupform_with_validation_with_input(self):
        form = SignUpForm(
            data={
                'first_name':'firname',
                'email':'correct@email.com',
                'password1':'_Xxxxxxx',
                'password2':'_Xxxxxxx',
                })
        self.assertTrue(form.is_valid())
