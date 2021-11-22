from django.db import models
from django.contrib.auth.models import User
from restaurants.models import Products, Restaurant

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="preparing")
    order = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()

    class Meta:
        ordering = ['created_at']