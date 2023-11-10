from django import forms
from .models import order
from django import template
from django.forms import DateInput


register = template.Library()

class orderForm(forms.ModelForm):
    class Meta:
        model = order
        fields = ['farm_name', 'region', 'prefecture', 'canton', 'village', 'phone_number', 'production_type', 'area_unit', 'area', 'current_employees', 'start_date', 'required_workers', 'tasks_to_perform', 'work_schedule']
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
        }
@register.filter(name='add_class')
def add_class(value, arg):
    css_classes = value.field.widget.attrs.get('class', '')
    value.field.widget.attrs['class'] = f'{css_classes} {arg}'
    return value

