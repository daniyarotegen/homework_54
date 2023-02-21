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


def update_view(request: WSGIRequest, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'GET':
        return render(request, 'category_update.html', context={'category': category})
    category.name = request.POST.get('name')
    category.description = request.POST.get('description')
    category.save()
    return redirect('categories')


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories')
    context = {
        'category': category,
    }
    return render(request, 'delete_category.html', context)