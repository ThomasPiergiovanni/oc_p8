from django.db import models

from authentication.models import CustomUser

# Create your models here.

class Category(models.Model):
    id_origin = models.CharField(max_length=200)
    name = models.CharField(max_length=200, unique=True)
    url = models.URLField(max_length=200, null=True)


class Product(models.Model):
    id_origin = models.CharField(max_length=200)
    name = models.CharField(max_length=200, unique=True)
    nutriscore_grade = models.CharField(max_length=8)
    fat = models.DecimalField(max_digits=8, decimal_places=3)
    saturated_fat = models.DecimalField(max_digits=8, decimal_places=3)
    sugar = models.DecimalField(max_digits=8, decimal_places=3)
    salt = models.DecimalField(max_digits=8, decimal_places=3)
    image = models.URLField(max_length=200)
    url = models.URLField(max_length=200)
    categories = models.TextField()
    category = models.ForeignKey(Category, models.CASCADE)
    relation_user = models.ManyToManyField(CustomUser, through='Favorites')

    def __str__(self):
        return self.name


class Favorites(models.Model):
    custom_user = models.ForeignKey(CustomUser, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)

    def __str__(self):
        return self.user.email
