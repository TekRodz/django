from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    imageURL = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)