# marketlink/urls.py

from django.urls import path
from .views import check_product_availability, submit_product_form

app_name = 'marketlink'

urlpatterns = [
    path('check_availability/<int:product_id>/', check_product_availability, name='check_product_availability'),
    path('submit_form/', submit_product_form, name='submit_product_form'),
    # Ajoutez d'autres patterns d'URL au besoin
]
