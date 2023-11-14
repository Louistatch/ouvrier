# marketlink/forms.py

from django import forms
from .models import Product, ProductCategory
from django.forms import DateInput

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'seller_name',
            'product_category',
            'region',
            'address',
            'status',
            'unit',
            'unit_price',
            'is_product_available',
            'quantity_available',
            'quantity_to_produce',
            'availability_date',
            'phone_number',
            'email',
        ]
        
        widgets = {
            'availability_date': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['product_category'].queryset = ProductCategory.objects.all()  