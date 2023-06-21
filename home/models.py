from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# tite


class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Address = models.CharField(max_length=600)


class Product(models.Model):
    product_name = models.CharField(max_length=600)
    description = models.CharField(max_length=69000)
    price = models.FloatField()


class Orders(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    delivered = models.BooleanField()


class Cart:
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField()
