from django import forms

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Set placeholders, class and autofocus to first field of form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_street_1': 'Street Address 1',
            'default_street_2': 'Street Address 2',
            'default_county': 'County',
            'default_postcode': 'Postcode',
        }
        self.fields['default_street_1'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False
