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
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)