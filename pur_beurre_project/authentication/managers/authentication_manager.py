from django.contrib.auth import authenticate, login, logout


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
    
    def _authenticate(self, email, password):
        """
        """
        return authenticate(email=email, password=password)
