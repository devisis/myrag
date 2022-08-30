from django.shortcuts import (
    render, redirect, get_object_or_404, reverse, HttpResponse
)
from django.contrib import messages
from products.views import view_product
from products.models import Product


def view_basket(request):
    """A view to return the basket content"""

    return render(request, "basket/basket.html")


def add_to_basket(request, durag_id):
    """ Add durag of a certain quantity to bag """

    quantity = int(request.POST.get('quantity'))
    durag = get_object_or_404(Product, pk=durag_id)
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if durag_id in list(basket.keys()):
        basket[durag_id] += quantity
    else:
        basket[durag_id] = quantity

    request.session['basket'] = basket
    print('if ', durag_id)
    print('is in > list basket keys', list(basket.keys()))
    print('this many > quaintity', quantity)
    print('plus this many // else equal to this many > basket id', basket[durag_id])
    print('request basket session', request.session['basket'])

    messages.success(request, f'Added {quantity} {durag.name}')
    return redirect(view_basket)


def update_basket(request, durag_id):
    """ Raise or lower quantity """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    durag = get_object_or_404(Product, pk=durag_id)

    if quantity > 0:
        basket[durag_id] = quantity
        messages.success(request, f'Updated {durag.name}')
    else:
        del basket[durag_id]
        messages.warning(request, f'Removed {durag.name}')

    request.session['basket'] = basket
    return redirect(view_basket)


def delete_basket(request, durag_id):
    """ Remove durags from the shopping bag """

    try:
        basket = request.session.get('basket', {})
        durag = get_object_or_404(Product, pk=durag_id)

        if basket[durag_id]:
            del basket[durag_id]
            messages.success(request, f'removed {durag.name}')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error: {e}')
        return HttpResponse(status=500)
