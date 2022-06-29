from django.shortcuts import get_object_or_404
from products.models import Product


def basket_items(request):

    basket_durags = []
    total = 0
    counter = 0
    basket = request.session.get('basket', {})

    for id, quantity in basket.items():
        durag = get_object_or_404(Product, pk=id)
        total += quantity * durag.price
        counter += quantity
        basket_durags.append({
            'id': id,
            'quantity': quantity,
            'durag': durag,
        })

    context = {
        'basket_durags': basket_durags,
        'total': total,
        'counter': counter,
        'basket': basket,
    }

    return context
