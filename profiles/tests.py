# from django.test import TestCase
import pytest
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse, resolve

from django.contrib.auth.models import User
from .models import Profile
from oc_lettings_site.settings import DEBUG


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
def test_profiles_index_view():
    client = Client()
    path = reverse('profiles:profiles_index')
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profile_view(fake_db):
    client = Client()
    user = fake_db["user"]
    path = reverse('profiles:profile',  kwargs={'username': user.username})
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")


@pytest.mark.django_db
def test_profiles_index_url():
    # Checks if the url named 'profiles_index' uses the 'profiles_index' view of the app lettings
    path = reverse('profiles:profiles_index')
    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles:profiles_index"


@pytest.mark.django_db
def test_profile_url(fake_db):
    # Checks if the url named 'profile' uses the 'profile' view of the app profiles
    user = fake_db["user"]
    path = reverse('profiles:profile', kwargs={'username': user.username})
    assert path == "/profiles/best_boss/"
    assert resolve(path).view_name == "profiles:profile"


@pytest.mark.django_db
def test_wrong_profile_object(fake_db):
    # Checks if the username of a non-existing user in the url triggers an error and the use of the customized error template
    # base_url/profile/"nobody"

    if DEBUG == False:
        client = Client()
        wrong_object_url = reverse("profiles:profile", kwargs={"username": "nobody"})
        response = client.get(wrong_object_url)
        assert response.status_code == 500
        assert assertTemplateUsed(response, "templates/500.html")
