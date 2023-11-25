# from django.test import TestCase
import pytest
from pytest_django.asserts import assertTemplateUsed
from django.test import Client
from django.urls import reverse, resolve
from .models import Address, Letting


@pytest.fixture
@pytest.mark.django_db
def fake_db():
    address = Address.objects.create(
            number = 55,
            street = "rue du Fbg Saint-Honoré",
            city = "Paris",
            state = "FRANCE",
            zip_code = 75008,
            country_iso_code = "FR")
    
    letting_site = Letting.objects.create(
            title = "Presidential private hotel in Paris",
            address_id = 1)
    
    return {"address": address, "letting_site": letting_site}



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
def test_letting_model(fake_db):
    client = Client()
    address = Letting.objects.create(
            title = "Luxury private hotel in Paris",
            address_id = 1)
    expected_value = "Luxury private hotel in Paris"
    assert str(address) == expected_value


@pytest.mark.django_db
def test_letting_index_view(fake_db):
    client = Client()
    # Letting.objects.create()
    path = reverse('lettings_index')
    response = client.get(path)
    content = response.content.decode()
    # expected_content = ""

    # assert content == expected_content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


# @pytest.mark.django_db
def test_letting_view(fake_db):
    client = Client()
    # Letting.objects.create()
    path = reverse('letting',  kwargs={'letting_id':1})
    response = client.get(path)
    content = response.content.decode()
    # expected_content = ""

    # assert content == expected_content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")


# @pytest.mark.django_db
def test_letting_index_url(fake_db):
    # Letting.objects.create()
    path = reverse('lettings_index')
    
    assert path == "lettings/"
    assert resolve(path).view_name == "lettings_index"


# @pytest.mark.django_db
def test_letting_url(fake_db):
    # Letting.objects.create()
    path = reverse('letting', kwargs={'letting_id':1})
    
    assert path == "lettings/1"
    assert resolve(path).view_name == "letting"


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