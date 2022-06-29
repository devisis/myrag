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
    """ Add durag of a certain quantity to bag """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if id in list(basket.keys()):
        basket[id] += quantity
    else:
        basket[id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    print("Quantity in add_to_basket:", quantity)
    print(type(quantity))
    messages.success(request, "test success")
    return redirect(view_product)
