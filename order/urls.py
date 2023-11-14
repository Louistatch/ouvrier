from django.urls import path
from .views import OrderFormView, OrderListView, BlogView, ServicesView, ContactView, ServiceUpdateView

app_name = 'order'


urlpatterns = [
    path('', OrderFormView.as_view(), name='order_form'),
    path('order_list/', OrderListView.as_view(), name='order_list'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('services/', ServicesView.as_view(), name='services'),
    path('contact/', ContactView.as_view(), name='contact'),  # Définissez la vue avec le nom 'contact'
    path('service_update/', ServiceUpdateView.as_view(), name='service_update'),

]
