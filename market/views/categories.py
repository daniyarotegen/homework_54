from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from market.models import Category


def c_add_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'category_create.html')
    category_data = {
        'name': request.POST.get('name'),
        'description': request.POST.get('description')
    }
    Category.objects.create(**category_data)
    return redirect('categories')


def c_index_view(request: WSGIRequest):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context=context)