from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from basket.contexts import basket_items


import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'street_1': request.POST['street_1'],
            'street_2': request.POST['street_2'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # Save form if form is valid
            order = order_form.save()
            for durag_id, quantity in basket.items():
                try:
                    # Get product id out of the basket and create line item
                    product = Product.objects.get(id=durag_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()

                except Product.DoesNotExist:
                    # If a product isnt found delete order and return user to
                    # the product page
                    messages.error(request, (
                        "A product in the basket isn't in our database!")
                    )
                    order.delete()
                    return redirect(reverse('durags'))

            # If user wants to save payment details redirect them
            # to checkout success page
            request.session['save-delivery'] = 'save-delivery' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number])
                )
        else:
            messages.error(request, 'Incorrect information entered. \
                Please double check the form.')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "Basket currently empty.")
            return redirect(reverse('durags'))

        current_basket = basket_items(request)
        total = current_basket['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.default_full_name,
                    'email': profile.user.email,
                    'street_1': profile.default_street_1,
                    'street_2': profile.default_street_2,
                    'county': profile.default_county,
                    'postcode': profile.default_postcode,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Your Stripe public key is missing. \
           Check your environment for missing keys.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    This will manage any successful checkouts
    """
    save_delivery = request.session.get('save_delivery')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

    if save_delivery:
        profile_data = {
            'default_street_1': order.street_1,
            'default_street_2': order.street_2,
            'default_county': order.county,
            'default_postcode': order.postcode,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Order successful! \
        Your order number: {order_number}. Check {order.email} \
        for a confirmation email.')

    if 'basket' in request.session:
        # delete users basket from session as it is no longer needed
        del request.session['basket']

    # set template and context
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
