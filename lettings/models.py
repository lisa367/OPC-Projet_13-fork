from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Class to create an address object in the database

    ...

    Attributes
    ----------
    number : int
        number of the street of the address
    street : str
        name of the street of the address
    city : str
        city of the address
    state : str
        state of the address
    zip_code : int
        zip code of the address
    country_iso_code : str
        coustry ISO code of the address

    Methods
    -------
    __str__:
        Prints the string representation of an address object
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'
    
    class Meta:
        verbose_name_plural = "Adresses"


class Letting(models.Model):
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Lettings"