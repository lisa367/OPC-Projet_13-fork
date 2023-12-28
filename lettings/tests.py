# from django.test import TestCase
import pytest
from pytest_django.asserts import assertTemplateUsed
from django.test import Client
from django.urls import reverse, resolve

from .models import Address, Letting
from oc_lettings_site.settings import DEBUG


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

    letting = Letting.objects.create(
            title = "Presidential private residence in Paris",
            address_id = 1)

    return {"address": address, "letting": letting}


@pytest.mark.django_db
def test_address_model(fake_db):
    address_object = fake_db["address"]
    expected_value = "55 rue du Fbg Saint-Honoré"
    assert str(address_object) == expected_value


@pytest.mark.django_db
def test_letting_model(fake_db):
    letting_object = fake_db["letting"]
    expected_value = "Presidential private residence in Paris"
    assert str(letting_object) == expected_value


@pytest.mark.django_db
def test_lettings_index_view():
    client = Client()
    path = reverse("lettings:lettings_index")
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_letting_object_view(fake_db):
    client = Client()
    path = reverse('lettings:letting',  kwargs={'letting_id': 1})
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")


@pytest.mark.django_db
def test_lettings_index_url():
    # Checks if the url named 'lettings_index' uses the 'lettings_index' view of the app lettings
    path = reverse('lettings:lettings_index')
    # path = "/lettings/"
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings:lettings_index"


@pytest.mark.django_db
def test_letting_url(fake_db):
    # Checks if the url named 'letting' ¸ uses the 'letting' view of the app lettings
    path = reverse('lettings:letting', kwargs={'letting_id': 1})
    # path = "/lettings/1"
    assert path == "/lettings/1/"
    assert resolve(path).view_name == "lettings:letting"


@pytest.mark.django_db
def test_wrong_letting_object(fake_db):
    # Checks if the id of a non-existing object in the url triggers an error and the use of the customized error template
    # base_url/lettings/0

    if DEBUG == False:
        client = Client()
        wrong_object_url = reverse("lettings:letting", kwargs={"letting_id": 0})
        response = client.get(wrong_object_url)
        assert response.status_code == 500
        assert assertTemplateUsed(response, "templates/500.html")
