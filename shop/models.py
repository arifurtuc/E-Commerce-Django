from django.db import models


class ProductCategory(models.Model):
    """
    Model representing product category.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    """
    Model representing product.
    """
    category = models.ForeignKey(
        ProductCategory, on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    image = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Model representing order details.
    """
    products = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total_price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
