""" Use session manager module
"""
from authentification.models import User

class UserSessionManager():
    """
    """
    def __init__(self):
        self.active = False
    
    def get_users(self):
        users = User.objects.all()
