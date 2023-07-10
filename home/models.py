from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# tite

class PersonalInformation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_lenght=100)
    ContactNumber = models.IntegerField()

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    zipcode = models.models.IntegerField()

    def __str__(self):
        return self.province


class Product(models.Model):
    product_name = models.CharField(max_length=600)
    product_image = models.ImageField(upload_to='items/', default='static/items/red_dress.jpg')
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.product_name

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name

class Orders(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    delivered = models.BooleanField()
    delivery_address = models.CharField(max_length=150)

    def __str__(self):
        return self.product_id

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return '{0} {1} {2}'.format(self.user_id, self.product_id, self.quantity)

class OrderDetails(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product_id