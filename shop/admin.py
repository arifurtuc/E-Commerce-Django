from django.contrib import admin
from .models import ProductCategory, Product, Order

# Configure Django admin settings
admin.site.site_header = "E-Commerce Admin"
admin.site.site_title = "E-Commerce"
admin.site.index_title = "Manage E-Commerce Shopping"


# Register models to make them accessible in the Django admin panel
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount_price', 'category')
    search_fields = ('name', 'description')
    list_editable = ('price', 'discount_price', 'category')


admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
