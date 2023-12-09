from django.db import models


class ProductCategory(models.Model):
    """
    Model representing product category.
    """
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

