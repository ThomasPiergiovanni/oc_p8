from django.db import models

# Create your models here.
class Category(models.Model):
    id_origin = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    id_origin = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    nutriscore_grade = models.CharField(max_length=8)
    fatty_acids = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    saturated_fatty_acids = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    sugar = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    salt = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    image = models.URLField(max_length=200, null=True)
    url = models.URLField(max_length=200, null=True)
    product_category = models.ManyToManyField(Category, through='Products')

    def __str__(self):
        return self.name


class Products(models.Model):
    product = models.ForeignKey(Product, models.CASCADE)
    category = models.ForeignKey(Category, models.CASCADE)

    def __str__(self):
        return self.product.name


class User(models.Model):
    first_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=200)
    user_products = models.ManyToManyField(Products, through='Favorites')

    def __str__(self):
        return self.email

class Favorites(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    products = models.ForeignKey(Products, models.CASCADE)

    def __str__(self):
        return self.user.email
