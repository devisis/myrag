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


def rag_details(request, product_id):
    """
    View to show detailed rag info
    """
    product = get_object_or_404(Product, pk=product_id)
    template = 'products/rag_details.html'
    context = {
        'product': product,
    }
    return render(request, template, context)


@login_required
def create_product(request):
    """ Add a durag to the store """
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        # if the form is valid save it send a message
        #  redirect user back to an empty form
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


@login_required
def edit_product(request, product_id):
    """ Update existing durag """
    # set product to equal the instance established by the primary key
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES, instance=product)
        # if the form is valid add success message and redirect to all durag page
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('durags'))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = AddProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product_form.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete selected durag """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Durags deleted!')
    return redirect(reverse('durags'))


def delete_all_products(request):
    """Delete all durags """
    products = Products.object.all()
    products.delete()
    messages.success(request, 'All durags deleted!')
    return redirect(reverse('durags'))
