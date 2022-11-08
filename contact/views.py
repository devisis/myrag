from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from contact.models import Contact
from .forms import ContactForm


def contact(request):
    """A view to return the contact page"""

    contact_form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid():
            messages.info(
                request, 'Thank you for your feedback.')
            return redirect(reverse('contact'))
    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)
