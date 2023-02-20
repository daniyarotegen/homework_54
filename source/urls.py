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
from market.views.categories import c_add_view
from market.views.index import index_view
from market.views.products import p_add_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_view, name='index'),
    path("product/add/", p_add_view, name='product_add'),
    path("category/add/", c_add_view, name='category_add'),
]
