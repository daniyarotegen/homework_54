from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'cost', 'added_datetime')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    ordering = ('-added_datetime',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
