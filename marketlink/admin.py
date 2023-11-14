# marketlink/admin.py

from django.contrib import admin
from .models import Product, ProductCategory

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'seller_name',
        'product_category',
        'region',
        'address',
        'status',
        'unit',
        'is_product_available',
        'quantity_available',
        'quantity_to_produce',
        'availability_date',
        'phone_number',
        'email',
        'submission_date',
    )
    list_filter = ('region', 'status', 'unit', 'is_product_available')
    search_fields = ('seller_name', 'product_category__name', 'region', 'status', 'unit', 'is_product_available')

    actions = ['delete_selected']

admin.site.register(Product, ProductAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    actions = ['delete_selected']

admin.site.register(ProductCategory, ProductCategoryAdmin)
