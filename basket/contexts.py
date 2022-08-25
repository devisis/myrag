from django.shortcuts import get_object_or_404
from django.conf import settings
from products.models import Product
from decimal import Decimal


def basket_items(request):

    basket_durags = []
    total = 0
    durag_count = 0
    basket = request.session.get('basket', {})

    for durag_id, quantity in basket.items():
        durag = get_object_or_404(Product, pk=durag_id)
        durag_count += quantity
        total += durag_count * durag.price
        basket_durags.append({
            'durag_id': durag_id,
            'quantity': quantity,
            'durag': durag,
            'durag_count': durag_count,
        })

    context = {
        'basket_durags': basket_durags,
        'total': total,
        'durag_count': durag_count,
        'basket': basket,
    }

    return context
