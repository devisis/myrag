from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from .forms import AddProductForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User


def view_product(request):
    """
    View to show all products
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/all_rags.html', context)


class AddProductView(SuccessMessageMixin, CreateView):

    model = Product
    form_class = AddProductForm
    template_name = 'product_create_form.html'
    success_url = '/products/create/'
    success_message = 'Product created!'

    # Ensure form is valid before saving it

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)
