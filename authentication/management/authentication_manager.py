# pylint: disable=R0201, R0903
"""Authentication manager module.
"""
from django.contrib.auth import authenticate, login, logout

from authentication.models import CustomUser


class AuthenticationManager():
    """Authentication manager class.
    """
    def _login(self, request, user):
        """ Method that logs in an authenticated user.
        """
        return login(request, user)

    def _logout(self, request):
        """Method that logs out a user.
        """
        return logout(request)

    def _authenticate(self, form_cleaned_data):
        """Method that authenticate a user based on its credentials.
        """
        return authenticate(
            email=form_cleaned_data['username'],
            password=form_cleaned_data['password']
        )

    def _create_user(self, form_cleaned_data):
        """Method use to create a user.
        """
        CustomUser.objects.create_user(
            email=form_cleaned_data['email'],
            password=form_cleaned_data['password1'],
            first_name=form_cleaned_data['first_name']
        )
