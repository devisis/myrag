from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Newsletter
from .forms import NewsletterForm


def newsletter(request):
    """A view to return the newsletter page"""

    newsletter_form = NewsletterForm(request.POST or None)
    if request.method == 'POST':
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(request, 'Successfully signed up. Thank You!')
            return redirect('index')

    template = 'newsletter/newsletter.html'
    context = {
        'newsletter_form': products,
    }

    return render(request, template, context)
