from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect(reverse('courses'))
        
    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
        'stripe_public_key': 'pk_test_51NJwhODYrsZEZMeamTyI0MaNhUObIxk13l9H8d3JwiyjtYR95gJRaqB01m6vBaIYcUOfk1oLsx1Mntw1bwVJy4QD00me48OpNg' 
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
