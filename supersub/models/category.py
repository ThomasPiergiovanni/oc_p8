"""Category module model
"""
from django.db import models


class Category(models.Model):
    """Category class model
    """
    id_origin = models.CharField(max_length=200)
    name = models.CharField(max_length=200, unique=True)
    url = models.URLField(max_length=200, null=True)
