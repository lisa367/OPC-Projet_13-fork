# from django.test import TestCase
import pytest
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse, resolve
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
@pytest.fixture
@pytest.mark.django_db
def fake_db():
    user = User.objects.create(
            password = "ABc1234!",
            username = "best_boss",
            first_name = "Michael",
            last_name = "Scott",
            email = "m.scott@dundermifflin.com")
    
    profile = Profile.objects.create(
            user_id = 1,
            favorite_city = "Paris")
    
    return {"user": user, "profile": profile}


@pytest.mark.django_db 
def test_profile_model(fake_db):
    profile = fake_db["profile"]
    expected_value = "best_boss"
    assert str(profile) == expected_value


@pytest.mark.django_db 
def test_profile_index_view():
    client = Client()
    Profile.objects.create()
    path = reverse('profiles_index')
    response = client.get(path)
    content = response.content.decode()
    # expected_content = ""

    # assert content == expected_content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db 
def test_profile_view():
    client = Client()
    user = User.objects.create(username = "test_user2", email="test_user2@fauxmail.com" )
    Profile.objects.create()
    path = reverse('profile',  kwargs={'username':"test_user3"})
    response = client.get(path)
    content = response.content.decode()
    # expected_content = ""

    # assert content == expected_content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")


@pytest.mark.django_db 
def test_profile_index_url():
    Profile.objects.create()
    path = reverse('profiles_index')
    
    assert path == "profiles/"
    assert resolve(path).view_name == "profiles_index"


@pytest.mark.django_db 
def test_profile_url():
    user = User.objects.create(username = "test_user3", email="test_user3@fauxmail.com" )
    Profile.objects.create()
    path = reverse('profile', kwargs={'username':"test_user3"})
    
    assert path == "profiles/3"
    assert resolve(path).view_name == "profile"



'''
@pytest.mark.django_db 
def test_profile_model():
    client = Client()
    user = User.objects.create(username = "test_user", email="test_user@fauxmail.com" )
    profile = Profile.objects.create(user=user.pk, favorite_city="Paris")
    expected_value = "test_user"
    assert str(profile) == expected_value

'''