from django.contrib.auth import authenticate, login, logout

from authentication.models import CustomUser


class AuthenticationManager():
    """
    """
    def _login(self, request, user):
        """
        """
        return login(request, user)

    def _logout(self, request):
        """
        """
        return logout(request)
    
    def _authenticate(self, form_cleaned_data):
        """
        """
        return authenticate(
            email=form_cleaned_data['username'],
            password=form_cleaned_data['password']
        )

    def _create_user(self, form_cleaned_data):
        CustomUser.objects.create_user(
            email=form_cleaned_data['email'],
            password=form_cleaned_data['password1'],
            first_name=form_cleaned_data['first_name']
        )
