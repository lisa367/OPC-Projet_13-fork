# from django.test import TestCase
import pytest
from django.test import Client
from .models import Address, Letting

# Create your tests here.
@pytest.mark.django_db  
def test_address_model():
    client = Client()
    address = Address.objects.create(
            number = 55,
            street = "rue du Fbg Saint-Honoré",
            city = "Paris",
            state = "FRANCE",
            zip_code = 75008,
            country_iso_code = "FR")
    expected_value = "55 rue du Fbg Saint-Honoré"
    assert str(address) == expected_value


@pytest.mark.django_db 
def test_letting_model():
    client = Client()
    address = Letting.objects.create(
            title = "Luxury private hotel in Paris",
            address = 1)
    expected_value = "Luxury private hotel in Paris"
    assert str(address) == expected_value


def test_letting_index_view():
    pass


def test_letting_view():
    pass


def test_letting_index_url():
    pass


def test_letting_url():
    pass
""" 
@pytest.mark.django_db  
def test_book_model():
    client = Client()
    book = Book.objects.create(
               author = "Jules Verne",
               title = "20 milles lieues sous les mers")
    expected_value = "Jules Verne | 20 milles lieues sous les mers"
    assert str(book) == expected_value
"""