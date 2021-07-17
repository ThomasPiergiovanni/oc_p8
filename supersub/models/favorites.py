# pylint: disable=E1101
"""Favorites module model
"""
from django.db import models

from authentication.models import CustomUser
from supersub.models.product import Product


class Favorites(models.Model):
    """Favorites class model. Composed of Custom User and Product classes
    foreign keys
    """
    custom_user = models.ForeignKey(CustomUser, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)

    def __str__(self):
        return self.custom_user.email
