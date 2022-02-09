import os
import django


import pytest
from django.shortcuts import reverse
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'support.settings')
django.setup()
from rest_framework import status

from chat.api.v1.serializers.message import MessageListSerializer
from tests.fixtures import user_object, user_data, api_client, user_client
from tests.test_message.fixtures import message_object, message_data
from tests.test_ticket.fixtures import ticket_object, ticket_data


urls = {
    'list': reverse('message_v1-list'),
    'create': reverse('message_v1-list'),
    'get_messages_by_id': ('/api/v1/chat/message/'),
}


@pytest.mark.django_db
def test_get_message_list_request(message_object, user_client):
    response = user_client.get(urls.get('list'), format='json')
    data = [MessageListSerializer(message_object).data]
    assert response.status_code == status.HTTP_200_OK
    # assert response.data == data


@pytest.mark.django_db
def test_post_message_request(message_data, user_client):
    response = user_client.post(urls.get('create'), data=message_data)
    print(response.data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_get_message_by_id(message_object, user_client, ticket_object):
    response = user_client.get(f"{urls.get('get_messages_by_id')}{ticket_object.id}/", format='json')
    data = [MessageListSerializer(message_object).data]
    assert response.status_code == status.HTTP_200_OK
    assert response.data == data
