from django.contrib import admin

from market.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_filter = ('id', 'name', 'description')
    search_fields = ('id', 'name', 'description')
    fields = ('id', 'name', 'description')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'added_datetime', 'cost')
    list_filter = ('id', 'name', 'category')
    search_fields = ('id', 'name', 'description')
    readonly_fields = ('id', 'added_datetime')
    fields = ('id', 'name', 'category', 'added_datetime', 'cost')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
