from django.contrib import admin
from .models import Product

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    fields = ['product_name', 'description', 'price', 'product_image']

admin.site.register(Product, ProductsAdmin)