from django.shortcuts import render, get_object_or_404
from .models import Letting

# View to display the list of all the lettings in the database
def lettings_index(request):
    """View to display the list of all the lettings in the database

    Args:
        request (_type_): The request passed from the url

    Returns:
        _type_: Returns the template that displays the list of the lettings objects in the database.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# View to display the details of one particular letting
def letting(request, letting_id):
    """View to display the details of one particular letting object from the database

    Args:
        request (_type_): The request pqssed from the url
        letting_id (int): The id of the letting to retrieve from the database, passed as a url argument

    Returns:
        _type_: Returns the template that displays the information of one letting object
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
