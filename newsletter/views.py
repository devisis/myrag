from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product
# from .forms import NewsletterForm


def newsletter(request):
    """A view to return the newsletter page"""

    products = Product.objects.all()
    template = 'newsletter/newsletter.html'
    context = {
        'newsletter_form': products,
    }

    return render(request, template, context)
