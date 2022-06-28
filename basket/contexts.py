
def basket_items(reqest):

    basket_durags = []
    total = 0
    counter = 0

    context = {
        'basket_durags': basket_durags,
        'total': total,
        'counter': counter,
    }

    return context
