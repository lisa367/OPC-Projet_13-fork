from django.shortcuts import render


def index(request):
    """View to access the landing page of the web app

    Args:
        request (request): Request passed from the url

    Returns:
        _type_: Returns the template that displays the homepage of the web app
    """
    return render(request, 'index.html')
