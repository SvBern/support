import pytest
from django.contrib.auth.models import User
from faker import Faker
from rest_framework.test import APIClient


@pytest.fixture
def user_data():
    faker = Faker()
    return {
        'email': faker.email(),
        'first_name': faker.first_name(),
        'last_name': faker.last_name(),
        'password': faker.password(),
        'username': faker.name(),
    }


@pytest.fixture
def user_object(user_data):
    return User.objects.create(**user_data)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_client(api_client, user_object):
    api_client.force_authenticate(user_object)
    return api_client
