from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)

class Products(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    restaurants = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)

