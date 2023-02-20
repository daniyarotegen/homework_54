from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Description')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Description')
    category = models.ForeignKey(
        to='market.Category',
        null=False,
        blank=False,
        related_name='product',
        verbose_name='Product',
        on_delete=models.CASCADE)
    added_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Added datetime')
    cost = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False, verbose_name='Cost')
    image = models.URLField(blank=True, verbose_name='Image URL')

    def __str__(self):
        return self.name
