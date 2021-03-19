from django.db import models

# Create your models here.
class Category(models.Model):
    id_origin = models.Charfield(max_lenght=200)
    name = models.Charfield(max_lenght=200)
    url = models.URLField(max_lenght=200)