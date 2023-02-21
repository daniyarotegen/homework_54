"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from market.views.categories import add_category, update_category, delete_category, view_category
from market.views.index import index_view
from market.views.products import add_product, view_product, delete_product, update_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_view, name='index'),
    path("product/add/", add_product, name='product_add'),
    path("category/add/", add_category, name='category_add'),
    path('product/<int:pk>', view_product, name='product_detail'),
    path('categories/', view_category, name='categories'),
    path('category/<int:pk>/update/', update_category, name='category_update'),
    path('product/<int:pk>/update/', update_product, name='product_update'),
    path('category/<int:pk>/delete/', delete_category, name='category_delete'),
    path('product/<int:pk>/delete/', delete_product, name='product_delete'),
]
