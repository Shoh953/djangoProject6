from django.shortcuts import render
from apps.models import Product


def product(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'limupa-digital-products-store-ecommerce/single-product.html', context)
