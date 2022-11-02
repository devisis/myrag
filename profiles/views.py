from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the profile information. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        # Create new form instance using post data
        # Instance being updated is the request users profile
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated!')
        else:
            messages.error(
                request,
                'Form invalid. Please try again with valid inputs.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ A view to show past orders """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is the history for order number: {order_number}.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
