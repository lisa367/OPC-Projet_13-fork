from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Class to create a profile object in the database

    ...

    Attributes
    ----------
    user : int
        foreign key of the user related to the profile
    favorite_city : str
        name of the favorite city of the profile

    Methods
    -------
    __str__():
        Prints the string representation of an profile object
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = "Profiles"