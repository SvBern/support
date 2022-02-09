import os
import django


import pytest
from django.shortcuts import reverse


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'support.settings')
django.setup()
from rest_framework import status
from chat.api.v1.serializers.ticket import TicketSerializer, TicketDetailSerializer
from tests.fixtures import user_object, user_data, api_client, user_client
from tests.test_message.fixtures import message_object, message_data
from tests.test_ticket.fixtures import ticket_object, ticket_data


urls = {
    'list': reverse('ticket_v1-list'),
    'create': reverse('ticket_v1-list'),
    'retrieve': ('/api/v1/chat/ticket/'),
}


@pytest.mark.django_db
def test_get_ticket_list_request(ticket_object, user_client):
    response = user_client.get(urls.get('list'), format='json')
    data = [TicketSerializer(ticket_object).data]
    assert response.status_code == status.HTTP_200_OK
    # assert response.data == data


@pytest.mark.django_db
def test_post_ticket_request(ticket_data, user_client):
    response = user_client.post(urls.get('create'), data=ticket_data)
    print(response.data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_get_ticket_by_id_request(ticket_object, user_client):
    response = user_client.get(f"{urls.get('retrieve')}{ticket_object.id}/", format='json')
    data = TicketDetailSerializer(ticket_object).data
    assert response.status_code == status.HTTP_200_OK
    assert response.data == data
