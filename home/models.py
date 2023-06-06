from django.db import models

# Create your models here.

class Users(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=240)

class Product(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=600)
    description = models.CharField()
    price = models.FloatField()

class Orders(models.Model):
    order_id = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
