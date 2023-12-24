from django.contrib import admin
from .models import ProductCategory, Product, Order

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Order)
