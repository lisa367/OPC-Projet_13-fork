# from django.test import TestCase
import pytest
from django.test import Client
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
@pytest.mark.django_db 
def test_profile_model():
    client = Client()
    user = User.objects.create(username = "test_user", email="test_user@fauxmail.com" )
    profile = Profile.objects.create(user=user.pk, favorite_city="Paris")
    expected_value = "test_user"
    assert str(profile) == expected_value

def test_profile_index_view():
    pass


def test_profile_view():
    pass


def test_profile_index_url():
    pass


def test_profile_url():
    pass
