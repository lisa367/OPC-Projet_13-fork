from django.shortcuts import render, get_object_or_404
from .models import Profile


def profiles_index(request):
    """View to display the list of all the profiles in the database

    Args:
        request (request): _description_

    Returns:
        _type_: _description_
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """View to display the details of one profile object from the database

    Args:
        request (_type_): The request pqssed from the url
        username (int): The username of user associated with the profile to retrieve from the database, passed as a url argument

    Returns:
        _type_: Returns the template that displays the information of one profile object
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)