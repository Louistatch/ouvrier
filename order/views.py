from django.urls import reverse
from django.views.generic import FormView, ListView, TemplateView
from .models import order
from .forms import orderForm

class OrderFormView(FormView):
    template_name = 'order_form.html'
    form_class = orderForm

    def get_success_url(self):
        return reverse('order_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class OrderListView(ListView):
    model = order
    template_name = 'order_list.html'
    context_object_name = 'orders'


class BlogView(TemplateView):
    template_name = 'blog.html'

class ServicesView(TemplateView):
    template_name = 'services.html'
    
class ContactView(TemplateView):
    template_name = 'contact.html'
    