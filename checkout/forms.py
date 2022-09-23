from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name', 'email', 'street_1', 'street_2',
            'county', 'postcode',
        )

    def __init__(self, *args, **kwargs):
        """
        Set placeholders, class and autofocus to first field of form
        """
        super().__init__(*args, **kwargs)
        # placeholders = {
        #     'full_name': 'Full Name',
        #     'email': 'Email Address',
        #     'street_1': 'Street Address 1',
        #     'street_2': 'Street Address 2',
        #     'county': 'County',
        #     'postcode': 'Postcode',
        # }
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            new_data = {
                'placeholder': str(field),
                'class': 'form-control'
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )
