from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Product, Category
from .forms import AddProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def view_product(request):
    """
    View to show all products
    """
    products = Product.objects.all()
    template = 'products/all_rags.html'
    context = {
        'products': products,
    }
    return render(request, template, context)


@login_required
def create_product(request):
    """ Add a durag to the store """
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        # if the form is valid save it send a message and redirect user back to an empty form
        if form.is_valid():
            form.save()
            messages.success(request, 'A new durag has been added!')
            return redirect(reverse('create_product'))
        else:
            messages.error(request, 'Failed to add a new durag. Check form is valid.')
    else:
        form = AddProductForm()

    template = 'products/product_create_form.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
