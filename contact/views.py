from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product
# from .forms import contactForm


def contact(request):
    """A view to return the contact page"""

    products = Product.objects.all()
    template = 'contact/contact.html'
    context = {
        'contact_form': products,
    }

    return render(request, template, context)
