from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    """
       Newsletter sign up form
    """
    class Meta:
        model = Newsletter
        fields = '__all__'
