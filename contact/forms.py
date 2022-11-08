from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
       Contact Us form
    """
    class Meta:
        model = Contact
        fields = '__all__'
