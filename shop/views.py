from django.views.generic import ListView
from .models import Product


class IndexView(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_list = Product.objects.all()

        # Search product
        product_name = self.request.GET.get('product_name')
        if product_name != '' and product_name is not None:
            product_list = product_list.filter(name__icontains=product_name)

        context['products'] = product_list
        return context
