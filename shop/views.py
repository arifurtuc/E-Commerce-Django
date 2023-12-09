from django.views.generic import ListView
from .models import Product


class IndexView(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'
