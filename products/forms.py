from django import forms
from .models import Product, Category


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Set placeholders, class and autofocus to first field of form
        """
        super().__init__(*args, **kwargs)
        cat = Category.objects.all()
        # create list of friendly names attached to category ids
        friendly_names = [(c.id, c.get_friendly_name()) for c in cat]

        #  use freindly name as field choices instead of id
        self.fields['category'].choices = friendly_names

        # add bootstrap classes to customise fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'text-white border border-info rounded-sm'
