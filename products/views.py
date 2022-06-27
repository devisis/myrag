from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from .models import Product
from django.contrib import messages


def view_product(request):
    """
    View to show all products
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/all_rags.html', context)


def add_to_basket(request, id):
    messages.success(request, "test success")
    return redirect(view_product)
