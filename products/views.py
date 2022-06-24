from django.shortcuts import render
from django.views import View
from .models import Product


def view_product(request):
    """
    View to show all products
    """
    products = Product.objects.all()

    if request.GET:
        return render(request, 'products/all_rags.html')