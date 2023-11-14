# marketlink/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def submit_product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Logique de traitement du formulaire ici (sauvegarde en base de données, etc.)
            product = form.save()  # Save the product and get the instance
            return redirect('marketlink:check_product_availability', product_id=product.id)  # Pass the product ID
    else:
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'marketlink/submit_form.html', context)

def check_product_availability(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
 
    if product.product_category.is_market_available:
        # Product is available
        context = {
            'message': 'Le marché est disponible!',
            'price': product.unit_price,
            'contact': 'Contactez Agrocrown pour vendre votre produit.'
        }
    else:
        # Product is not available
        context = {
            'message': 'Le marché n\'est pas encore disponible. Agrocrown est en charge et vous reviendra bientôt.'
        }

    return render(request, 'marketlink/product_availability.html', context)




