from django.contrib import admin
from .models import *

class CategoryInline(admin.TabularInline):
    model = Category

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    fields = ['product_name', 'description', 'price', 'product_image']
    inlines = [CategoryInline]


class CategoryAdmin(admin.ModelAdmin):
    fields = ['category_name']

admin.site.register(Product, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)