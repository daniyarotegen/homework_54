from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from market.models import Product, Category


def p_add_view(request: WSGIRequest):
    categories = Category.objects.all()
    if request.method == 'GET':
        return render(request, 'product_create.html', {'categories': categories})
    name = request.POST.get('name')
    description = request.POST.get('description')
    category_id = request.POST.get('category')
    category = Category.objects.get(pk=category_id)
    cost = request.POST.get('cost')
    image = request.POST.get('image')
    product = Product.objects.create(name=name, description=description, category=category, cost=cost, image=image)
    return redirect('product_detail', pk=product.pk)


def p_detailed_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product})


def p_update_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()
    if request.method == 'GET':
        return render(request, 'product_update.html', context={'product': product, 'categories': categories})
    product.name = request.POST.get('name')
    product.description = request.POST.get('description')
    category_id = request.POST.get('category')
    product.category = Category.objects.get(pk=category_id)
    product.cost = request.POST.get('cost')
    product.image = request.POST.get('image')
    product.save()
    return redirect('product_detail', pk=product.pk)
