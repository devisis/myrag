from django.shortcuts import render


def view_basket(request):
    """Aview to return the basket content"""

    return render(request, "basket/basket.html")
