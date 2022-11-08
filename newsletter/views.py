from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from newsletter.models import Newsletter
from .forms import NewsletterForm


def newsletter(request):
    """A view to return the newsletter page"""

    newsletter_form = NewsletterForm(request.POST or None)
    if request.method == 'POST':
        if newsletter_form.is_valid():
            current = newsletter_form.save(commit=False)
            if Newsletter.objects.filter(email=current.email).exists():
                messages.info(
                    request, 'You have already subscribed.')
                return redirect(reverse('home'))
            else:
                newsletter_form.save()
                messages.success(request, 'Successfully signed up. Thank You!')
                return redirect('home')

    template = 'newsletter/newsletter.html'
    context = {
        'newsletter_form': newsletter_form,
    }

    return render(request, template, context)
