# from django.test import TestCase
import pytest
from pytest_django.asserts import assertTemplateUsed
from django.test import Client
from django.urls import reverse, resolve


def test_index_view():
    client = Client()
    path = reverse('index')
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")


@pytest.mark.django_db
def test_index_url():
    path = reverse('index')
    assert path == "/"
    assert resolve(path).view_name == "index"
