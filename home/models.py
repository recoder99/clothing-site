from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
# tite


class PersonalInformation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    province = models.CharField(max_length=100, blank=True)
    zipcode = models.IntegerField(blank=True, null=True)
    ContactNumber = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user_id.first_name
    
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

def upload_location(instance, filename):
    return "items/{0}_{1}".format(datetime.now().strftime("%m%d%y-%H%M%S"), filename)

class Product(models.Model):
    product_name = models.CharField(max_length=600)
    product_image = models.ImageField(upload_to=upload_location, default='static/items/red_dress.jpg')
    description = models.TextField()
    category_name = models.ManyToManyField(Category)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sold = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
    
class Orders(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    delivered = models.BooleanField()
    pay_method = models.CharField(max_length=100, null=True)
    delivery_address = models.CharField(max_length=150)

    def __str__(self):
        return str(self.pk)
    

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
        return self.order_id.pk