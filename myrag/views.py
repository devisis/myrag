from django.shortcuts import render


def error_handler_404(request, exception):
    """ View to display Handler 404 - Error page """
    return render(request, 'errors/404.html', status=404)
