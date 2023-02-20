from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from market.models import Product, Category


def index_view(request: WSGIRequest):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'index.html', context=context)