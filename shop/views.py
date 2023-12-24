from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Product, Order


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

        # Pagination
        paginator = Paginator(product_list, 4)
        page = self.request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver the first page
            products = paginator.page(1)
        except EmptyPage:
            # If page is out of range , deliver the last page of results
            products = paginator.page(paginator.num_pages)

        context['products'] = products
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/detail.html'
    context_object_name = 'product'


def checkout(request):
    if request.method == 'POST':
        products = request.POST.get('products', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zipcode = request.POST.get('zipcode', '')
        total_price = request.POST.get('total_price', '')

        order = Order(
            products=products, name=name, email=email, address=address,
            city=city, state=state, zipcode=zipcode, total_price=total_price
        )
        order.save()

    return render(request, 'shop/checkout.html')
