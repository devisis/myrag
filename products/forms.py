from django.forms import ModelForm
from django import forms
from .models import Product
from .models import Category
from django.core.exceptions import ValidationError


class AddProductForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        # widgets = {
        #     'category',
        #     'name',
        #     'style',
        #     'material',
        #     'color',
        #     'price',
        #     'featured_image',
        #     'description',
        # }
