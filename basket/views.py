from django.shortcuts import render, redirect
from django.contrib import messages
from products.views import view_product


def view_basket(request):
    """Aview to return the basket content"""

    return render(request, "basket/basket.html")


def add_to_basket(request, durag_id):
    """ Add durag of a certain quantity to bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    print(basket[durag_id])
    
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

    messages.success(request, "quantity test success")
    return redirect(view_basket)
