from django.db import models

# Create your models here.
class Category(models.Model):
    id_origin = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)


class Product(models.Model):
    id_origin = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    nutriscore_grade = models.CharField(max_length=8)
    fatty_acids = models.DecimalField(max_digits=8, decimal_places=3)
    saturated_fatty_acids = models.DecimalField(max_digits=8, decimal_places=3)
    sugar = models.DecimalField(max_digits=8, decimal_places=3)
    salt = models.DecimalField(max_digits=8, decimal_places=3)
    image = models.URLField(max_length=200)
    url = models.URLField(max_length=200)