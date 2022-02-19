from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    """ Check bag has content and render order template """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is currently empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KUt26G7L1c3WfQsIZbvw14td2508uyZrRdxNGNfW8KKIvdCGeRMeOyjQL9Q8fpAKpVDQ3A39LPVPWoz4NFnaN1L00Uc1yruc7',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
